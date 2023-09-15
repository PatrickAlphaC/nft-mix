#!/usr/bin/python3
from brownie import AdvancedCollectible, accounts, config
from scripts.helpful_scripts import get_breed, fund_with_link, listen_for_event
import time


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]

    transaction = advanced_collectible.createCollectible("None", {"from": dev})
    transaction.wait(1)
    # time.sleep(35)
    print("Waiting on randomWords VRFCoordinator fullfillment...")
    event = listen_for_event(
        advanced_collectible, "ReturnedCollectible", timeout=200, poll_interval=10
    )
    breed_id = event.args.breed
    token_id = event.args.newItemId
    breed = get_breed(breed_id)
    print("Dog breed of tokenId {} is {}".format(token_id, breed))
