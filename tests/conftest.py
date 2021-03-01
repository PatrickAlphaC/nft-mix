
import pytest
from brownie import config, network, accounts, MockV3Aggregator, VRFCoordinatorMock, LinkToken, Contract, MockOracle
import os


@pytest.fixture
def get_eth_usd_price_feed_address():
    if network.show_active() == 'development':
        mock_price_feed = MockV3Aggregator.deploy(
            18, 2000, {'from': accounts[0]})
        return mock_price_feed.address
    if network.show_active() in config['networks']:
        return config['networks'][network.show_active()]['eth_usd_price_feed']
    else:
        pytest.skip('Invalid network specified ')
        return


@pytest.fixture(scope="module")
def get_account():
    if network.show_active() == 'development' or network.show_active() == 'mainnet-fork':
        return accounts[0]
    if network.show_active() in config['networks']:
        dev_account = accounts.add(os.getenv(config['wallets']['from_key']))
        return dev_account
    else:
        pytest.skip('Invalid network/wallet specified ')


@pytest.fixture(scope="module")
def get_link_token(get_account):
    if network.show_active() == 'development' or 'fork' in network.show_active():
        link_token = LinkToken.deploy({'from': get_account})
        return link_token
    if network.show_active() in config['networks']:
        return Contract.from_abi(
            "link_token", config['networks'][network.show_active()]['link_token'], LinkToken.abi)
    else:
        pytest.skip('Invalid network/link token specified ')


@pytest.fixture
def get_vrf_coordinator(get_account, get_link_token):
    if network.show_active() == 'development' or 'fork' in network.show_active():
        mock_vrf_coordinator = VRFCoordinatorMock.deploy(
            get_link_token.address, {'from': get_account})
        return mock_vrf_coordinator
    if network.show_active() in config['networks']:
        vrf_coordinator = Contract.from_abi(
            "vrf_coordinator", config['networks'][network.show_active()]['vrf_coordinator'], VRFCoordinatorMock.abi)
        return vrf_coordinator
    else:
        pytest.skip('Invalid network specified')


@pytest.fixture
def get_keyhash(get_account, get_link_token):
    if network.show_active() == 'development' or 'fork' in network.show_active():
        return 0
    if network.show_active() in config['networks']:
        return config['networks'][network.show_active()]['keyhash']
    else:
        pytest.skip('Invalid network/link token specified ')


@pytest.fixture
def get_job_id():
    if network.show_active() == 'development' or 'fork' in network.show_active():
        return 0
    if network.show_active() in config['networks']:
        return config['networks'][network.show_active()]['jobId']
    else:
        pytest.skip('Invalid network/link token specified')


@pytest.fixture
def get_seed():
    return 777


@pytest.fixture
def get_data():
    return 100


@pytest.fixture
def get_oracle(get_link_token, get_account):
    if network.show_active() == 'development' or 'fork' in network.show_active():
        mock_oracle = MockOracle.deploy(
            get_link_token.address, {'from': get_account})
        return mock_oracle
    if network.show_active() in config['networks']:
        mock_oracle = Contract.from_abi(
            "mock_oracle", config['networks'][network.show_active()]['oracle'], MockOracle.abi)
        return mock_oracle
    else:
        pytest.skip('Invalid network specified')


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
