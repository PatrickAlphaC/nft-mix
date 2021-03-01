#!/usr/bin/python3
import os
from brownie import SimpleCollectible, accounts, network, config


def main():
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    print(network.show_active())
    simple_collectible = SimpleCollectible[len(SimpleCollectible) - 1]
    print(simple_collectible.ownerOf(0))
    return SimpleCollectible.deploy({'from': dev})
