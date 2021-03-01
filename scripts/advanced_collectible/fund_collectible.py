#!/usr/bin/python3
import os
from brownie import AdvancedCollectible, accounts, network, interface, config


def main():
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    # Get the most recent PriceFeed Object
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    interface.LinkTokenInterface(config['networks'][network.show_active()]['link_token']).transfer(
        advanced_collectible, config['networks'][network.show_active()]['fee'], {'from': dev})
