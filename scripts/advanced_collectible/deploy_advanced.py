#!/usr/bin/python3
import os
from brownie import AdvancedCollectible, accounts, network, config
# This loads the env file
from dotenv import load_dotenv
load_dotenv()


def main():
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    print(network.show_active())
    # publish_source = True if os.getenv("ETHERSCAN_TOKEN") else False # Currently having an issue with this
    publish_source = False
    return AdvancedCollectible.deploy(config['networks'][network.show_active()]['vrf_coordinator'],
                                      config['networks'][network.show_active()
                                                         ]['link_token'],
                                      config['networks'][network.show_active()
                                                         ]['keyhash'],
                                      {'from': dev}, publish_source=publish_source)
