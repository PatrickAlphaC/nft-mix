#!/usr/bin/python3
from brownie import AdvancedCollectible, accounts, network, config
from scripts.helpful_scripts import fund_with_link, get_publish_source

def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    advanced_collectible = AdvancedCollectible.deploy(
        config["networks"][network.show_active()]["vrf_coordinator"],
        config["networks"][network.show_active()]["subscriptionId"],
        config["networks"][network.show_active()]["keyHash"],
        {"from": dev},
        publish_source=get_publish_source(),
    )
    return advanced_collectible
