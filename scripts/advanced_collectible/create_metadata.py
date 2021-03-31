#!/usr/bin/python3
import os
from brownie import SimpleCollectible, AdvancedCollectible, accounts, network, config
from metadata import sample_metadata
import json
from scripts.helpful_scripts import get_breed
from pathlib import Path
# This loads the env file
from dotenv import load_dotenv
load_dotenv()

PUG_URI = 'https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png'


def main():
    # dev = accounts.add(os.getenv(config['wallets']['from_key']))
    print("Working on " + network.show_active())
    advanced_collectible = AdvancedCollectible[len(SimpleCollectible) - 1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(number_of_advanced_collectibles)
    write_metadata(number_of_advanced_collectibles, advanced_collectible)


def write_metadata(token_ids, nft_contract):
    for token_id in range(token_ids):
        collectible_metadata = sample_metadata.metadata_template
        breed = get_breed(nft_contract.tokenIdToBreed(token_id))
        metadata_file_name = './metadata/{}/'.format(network.show_active()) + \
            str(token_id) + "-" + breed + ".json"
        if Path(metadata_file_name).exists():
            print('{} already found, delete it to overwrite!'.format(
                metadata_file_name))
            continue
        else:
            print('Creating Metadata file: ' + metadata_file_name)
            collectible_metadata['name'] = get_breed(
                nft_contract.tokenIdToBreed(token_id))
            collectible_metadata['description'] = 'An adorable {} pup!'.format(
                collectible_metadata['name'])
            collectible_metadata['image'] = PUG_URI
            file = open(metadata_file_name, 'w')
            json.dump(collectible_metadata, file)
