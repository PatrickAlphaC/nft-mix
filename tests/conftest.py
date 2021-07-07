import pytest
from brownie import (
    accounts,
    config,
    network,
)
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


@pytest.fixture
def get_keyhash():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return 0
    if network.show_active() in config["networks"]:
        return config["networks"][network.show_active()]["keyhash"]
    else:
        pytest.skip("Invalid network/link token specified ")


@pytest.fixture
def get_job_id():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return 0
    if network.show_active() in config["networks"]:
        return config["networks"][network.show_active()]["jobId"]
    else:
        pytest.skip("Invalid network/link token specified")


@pytest.fixture
def get_data():
    return 100


@pytest.fixture
def dev_account():
    return accounts[0]


@pytest.fixture
def node_account():
    return accounts[1]


@pytest.fixture
def chainlink_fee():
    return 1000000000000000000


@pytest.fixture
def expiry_time():
    return 300
