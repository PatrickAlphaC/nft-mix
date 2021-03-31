#!/usr/bin/python3
import os
from brownie import SimpleCollectible, accounts, network, config
# This loads the env file
from dotenv import load_dotenv
load_dotenv()


def main():
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    print(network.show_active())
    publish_source = True if os.getenv("ETHERSCAN_TOKEN") else False
    simple_collectible = SimpleCollectible.deploy(
        {'from': dev}, publish_source=publish_source)
    simple_collectible.createCollectible("None")
    print(simple_collectible.ownerOf(0))
