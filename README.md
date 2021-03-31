# nft-mix

<br/>
<p align="center">
<a href="https://chain.link" target="_blank">
<img src="https://raw.githubusercontent.com/PatrickAlphaC/nft-mix/main/img/pug.png" width="225" alt="NFT Pug">
</a>
</p>
<br/>

This is a repo to work with and use NFTs smart contracts in a python environment, using the Chainlink-mix as a starting point. 

If you'd like to see another repo using random NFTs that are deployed to mainnet, check out the [D&D package](https://github.com/PatrickAlphaC/dungeons-and-dragons-nft).

## Prerequisites

Please install or have installed the following:

- [nodejs and npm](https://nodejs.org/en/download/)
- [python](https://www.python.org/downloads/)
## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already. Here is a simple way to install brownie.

```bash
pip install eth-brownie
```

2. Clone this repo
```
git clone https://github.com/PatrickAlphaC/nft-mix
cd nft-mix
```

3. [Install ganache-cli](https://www.npmjs.com/package/ganache-cli) and [openzepplin contracts](https://github.com/OpenZeppelin/openzeppelin-contracts)

```bash
npm install -g ganache-cli
npm install @openzeppelin/contracts
```


If you want to be able to deploy to testnets, do the following. 
4. Set your environment variables

Set your `WEB3_INFURA_PROJECT_ID`, and `PRIVATE_KEY` [environment variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html). 

You can get a `WEB3_INFURA_PROJECT_ID` by getting a free trial of [Infura](https://infura.io/). At the moment, it does need to be infura with brownie. You can find your `PRIVATE_KEY` from your ethereum wallet like [metamask](https://metamask.io/). 

You can add your environment variables to the `.env` file:
```
export WEB3_INFURA_PROJECT_ID=<PROJECT_ID>
export PRIVATE_KEY=<PRIVATE_KEY>
```

Or you can run the above in your shell. 


# Useage

There are 2 types of NFTs here. 
1. `SimpleCollectibles.sol`
2. `AdvancedCollectibles.sol`

They each deploy unique dogs. The advanced version gives you a random breed (out of a Pug, Shiba Inu, and St. Brenard).

The advanced collection uses a [Chainlink VRF](https://docs.chain.link/docs/get-a-random-number) to deploy the random dog. 

You can 100% use the rinkeby testnet to see your NFTs rendered on opensea, but it's suggested that you test and build on a local development network so you don't have to wait as long for transactions. 

### Running Scripts

The simple collectibles work on a local network,  however the advanced requires a testnet. We default to rinkeby since that seems to be the testing standard for NFT platforms. You will need testnet rinkeby ETH and testnet Rinkeby LINK. You can find faucets for both in the [Chainlink documentation](https://docs.chain.link/docs/link-token-contracts#rinkeby). 

# For the Simple ERC721
```
brownie run scripts/simple_collectible/deploy_simple.py --network rinkeby
brownie run scripts/simple_collectible/create_collectible.py --network rinkeby
```

# For the Advanced ERC721

You'll need [testnet Rinkeby](https://faucet.rinkeby.io/) and [testnet LINK](https://rinkeby.chain.link/) in the wallet associated with your private key. 

```
brownie run scripts/advanced_collectible/deploy_advanced.py --network rinkeby
brownie run scripts/advanced_collectible/create_collectible.py --network rinkeby
```
And after some time, (you may have to wait up to 20 minutes for it to render on opensea), you should see your NFT on opensea! [It'll look something like this.](https://testnets.opensea.io/assets/0x8acb7ca932892eb83e4411b59309d44dddbc4cdf/0)

## Verify on Etherscan

Currently, the advanced collectibles contract has an issue with ERC721 and the Chainlink contracts, so they have be verified manually. However, the simple contract can be verified if you just set your `ETHERSCAN_TOKEN`. 

### Misc
There are some helpful scripts in `helpful_scripts.py`.

# Viewing on OpenSea
After running the scripts from the `For the Advanced ERC721` section

1. Create the metadata
Run
```
brownie run scripts/advanced_collectible/create_metadata.py --network rinkeby
```
The metadata has already been created if you've just cloned the repo. 

2. SKIP THIS STEP IF YOU WANT TO USE PATRICK'S METADATA. Add the file created in `metadata/rinkeby/NAME.json` to [IPFS](https://ipfs.io/) or [Pinata](https://pinata.cloud/).
3. Set the tokenURI 
Run
```
brownie run scripts/advanced_collectible/set_tokenuri.py --network rinkeby
```
It may take some time for the image to render on opensea. So take your time here!
## Testing

```
brownie test
```

## Resources

To get started with Brownie:

* [Chainlink Documentation](https://docs.chain.link/docs)
* Check out the [Chainlink documentation](https://docs.chain.link/docs) to get started from any level of smart contract engineering. 
* Check out the other [Brownie mixes](https://github.com/brownie-mix/) that can be used as a starting point for your own contracts. They also provide example code to help you get started.
* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) is a good tutorial to help you familiarize yourself with Brownie.
* For more in-depth information, read the [Brownie documentation](https://eth-brownie.readthedocs.io/en/stable/).

Shoutout to [TheLinkMarines](https://twitter.com/TheLinkMarines) on twitter for the puppies!

Any questions? Join our [Discord](https://discord.gg/2YHSAey)

## License

This project is licensed under the [MIT license](LICENSE).
