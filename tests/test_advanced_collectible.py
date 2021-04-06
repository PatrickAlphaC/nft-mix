import pytest
from brownie import network, AdvancedCollectible


def test_can_create_advanced_collectible(
    get_account,
    get_vrf_coordinator,
    get_keyhash,
    get_link_token,
    chainlink_fee,
    get_seed,
):
    # Arrange
    if network.show_active() not in ["development"] or "fork" in network.show_active():
        pytest.skip("Only for local testing")
    advanced_collectible = AdvancedCollectible.deploy(
        get_vrf_coordinator.address,
        get_link_token.address,
        get_keyhash,
        {"from": get_account},
    )
    get_link_token.transfer(
        advanced_collectible.address, chainlink_fee * 3, {"from": get_account}
    )
    # Act
    transaction_receipt = advanced_collectible.createCollectible(
        "None", get_seed, {"from": get_account}
    )
    requestId = transaction_receipt.events["requestedCollectible"]["requestId"]
    assert isinstance(transaction_receipt.txid, str)
    get_vrf_coordinator.callBackWithRandomness(
        requestId, 777, advanced_collectible.address, {"from": get_account}
    )
    # Assert
    assert advanced_collectible.tokenCounter() > 0
    assert isinstance(advanced_collectible.tokenCounter(), int)
