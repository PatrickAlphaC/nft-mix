#!/usr/bin/python3
from brownie import SimpleCollectible, accounts, network, config


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    simple_collectible = SimpleCollectible[len(SimpleCollectible) - 1]
    return simple_collectible.createCollectible("None", {"from": dev})
