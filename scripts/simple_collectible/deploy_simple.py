#!/usr/bin/python3
import os
from brownie import SimpleCollectible, accounts, network, config
# This loads the env file
from dotenv import load_dotenv
load_dotenv()


def main():
    print(os.getenv("cat"))
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    print(network.show_active())
    simple_collectible = SimpleCollectible.deploy({'from': dev})
    simple_collectible.createCollectible("None")
    print(simple_collectible.ownerOf(0))
