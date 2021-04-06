import pytest
from brownie import network, SimpleCollectible, convert


def test_can_create_simple_collectible(get_account):
    simple_collectible = SimpleCollectible.deploy({"from": get_account})
    simple_collectible.createCollectible("None")
    assert simple_collectible.ownerOf(0) == get_account
