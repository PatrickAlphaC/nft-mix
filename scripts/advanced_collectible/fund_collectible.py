#!/usr/bin/python3
import os
from brownie import AdvancedCollectible, accounts, network, interface, config
from scripts.helpful_scripts import fund_advanced_collectible
# This loads the env file
from dotenv import load_dotenv
load_dotenv()


def main():
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    fund_advanced_collectible(advanced_collectible)
