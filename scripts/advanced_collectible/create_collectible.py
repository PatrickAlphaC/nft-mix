#!/usr/bin/python3
import os
from brownie import AdvancedCollectible, accounts, config
import time
# This loads the env file
from dotenv import load_dotenv
load_dotenv()

STATIC_SEED = 123


def get_breed(breed_number):
    switch = {
        0: "PUG",
        1: "SHIBA_INU",
        2: "BRENARD"
    }
    return switch[breed_number]


def main():
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    transaction = advanced_collectible.createCollectible(
        "None", STATIC_SEED, {'from': dev})
    print("Waiting on second transaction...")
    time.sleep(30)
    requestId = transaction.events['requestedCollectible']['requestId']
    token_id = advanced_collectible.requestIdToTokenId(requestId)
    breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
    print("Dog breed of tokenId {} is {}".format(token_id, breed))
