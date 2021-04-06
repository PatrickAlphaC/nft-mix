#!/usr/bin/python3
from brownie import AdvancedCollectible, accounts, network, config, interface
import json


def main():
    flatten()


def flatten():
    file = open("./AdvancedCollectible_flattened.json", "w")
    json.dump(AdvancedCollectible.get_verification_info(), file)
    file.close()
