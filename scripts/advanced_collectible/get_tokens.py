#!/usr/bin/python3
import os
from brownie import SimpleCollectible, AdvancedCollectible, accounts, network, config
from metadata import sample_metadata
from scripts.helpful_scripts import get_breed
from pathlib import Path
# This loads the env file
from dotenv import load_dotenv
load_dotenv()


def main():
    # dev = accounts.add(os.getenv(config['wallets']['from_key']))
    print("Working on " + network.show_active())
    advanced_collectible = AdvancedCollectible[len(SimpleCollectible) - 1]
    breakpoint()
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(number_of_advanced_collectibles)
