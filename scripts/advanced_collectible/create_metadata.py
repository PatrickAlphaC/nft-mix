#!/usr/bin/python3
import os
import requests
import json
from brownie import AdvancedCollectible, network
from metadata import sample_metadata
from scripts.helpful_scripts import get_breed
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


pug_uri = "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png"


def main():
    print("Working on " + network.show_active())
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(number_of_advanced_collectibles)
    write_metadata(number_of_advanced_collectibles, advanced_collectible)


def write_metadata(token_ids, nft_contract):
    for token_id in range(token_ids):
        collectible_metadata = sample_metadata.metadata_template
        breed = get_breed(nft_contract.tokenIdToBreed(token_id))
        metadata_file_name = (
            "./metadata/{}/".format(network.show_active())
            + str(token_id)
            + "-"
            + breed
            + ".json"
        )
        if Path(metadata_file_name).exists():
            print(
                "{} already found, delete it to overwrite!".format(metadata_file_name)
            )
            continue
        else:
            print("Creating Metadata file: " + metadata_file_name)
            collectible_metadata["name"] = get_breed(
                nft_contract.tokenIdToBreed(token_id)
            )
            collectible_metadata["description"] = "An adorable {} pup!".format(
                collectible_metadata["name"]
            )
            if os.getenv("UPLOAD_IPFS") == "true":
                pug_uri = upload_nft()
            collectible_metadata["image"] = pug_uri
            file = open(metadata_file_name, "w")
            json.dump(collectible_metadata, file)


def upload_nft(image_path="./img/pug.png"):
    with Path(image_path).open("rb") as fp:
        image_binary = fp.read()
    ipfs_url = (
        os.getenv("IPFS_URL")
        if os.getenv("IPFS_URL")
        else "https://ipfs.infura.io:5001/"
    )
    response = requests.post(ipfs_url + "/api/v0/add", files={"file": image_binary})
    ipfs_hash = response.json()["Hash"]
    filename = image_path.split("/")[-1:][0]
    image_uri = "https://ipfs.io/ipfs/{}?filename={}".format(ipfs_hash, filename)
    print(image_uri)
    return image_uri
