import pytest
from brownie import network, SimpleCollectible, convert
from scripts.helpful_scripts import get_account


def test_can_create_simple_collectible():
    if network.show_active() not in ["development"] or "fork" in network.show_active():
        pytest.skip("Only for local testing")
    simple_collectible = SimpleCollectible.deploy({"from": get_account()})
    simple_collectible.createCollectible("None")
    assert simple_collectible.ownerOf(0) == get_account()
