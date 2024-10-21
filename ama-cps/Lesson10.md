# Consensus for blockchain

*Note:* this part cannot be found in the usual book (at least not so in-depth)

## History

Anyone usually knows blockchain for cryptocurrency, in particular for Bitcoins. Bitcoin is just a value, a kind of money. Blockchain is what enables the existance of Bitcoins.

One of the main selling points is that this technology is decentralized and peer to peer.

It all started in 2008 when bitcoin.org was first registered. A paper was published by Satoshi Nakamoto with a software that allowed the mining of bitcoins. There were other technology like that one before but they weren't as usable and well thought.

Satoshi Nakamoto is indeed a pseudonym and the real identity of the person is still unknown.

## How it works

Every 10 minute a new block is added to the blockchain. This block contains all the transactions that happened in the last 10 minutes. The block is then broadcasted to the network and the network has to agree on the validity of the block.

In order to authenticate people must use a private key, if the key is lost there is no way to recover it and the money are therefore lost.

There are 3 phases of blockchain:

- **Blockchain 1.0**: the first blockchain was used for cryptocurrencies
- **Blockchain 2.0**: the second blockchain was used for smart contracts
- **Blockchain 3.0**: the third blockchain is used for distributed applications

## Handling Consensus

There are two ways to solve consensus:

- **Permissionless consensus:**
  - all nodes share rights
  - all nodes have the same possibilites
  - all nodes participate without having to ask
- **Permission consensus:**
  - nodes can have different rights from eachother
  - nodes must have permission from another node.

In blockchain we work with the first one.

### Some words

- **Mining:** the process of reaching an agreement
- **Block:** base structure of the blockchain
- **Miners:** those who participate in the algorithm

## POW

**Pow** is the first algorithm implemented in the blockchain and it's permissionless.

Each owner transfers the coin to the next by digitally signing a hash of the previous transaction and the public key of the next owner and adding these to the end of the coin. Someone who buys the coin can verify the signature of the whole chain.

**Problem:** the one who wants to buy the coin doesn't know if someone double spent the coin.

**Solution:** there must be a public announcement of each transaction. In this way everyone agrees on one chain and therefore ban double spending.

A **timestamp server** is like a newspaper, it contains info on the chain and by looking at it you know the current correct chain of a coin.

The way to obtain a coin is by scanning for a value that when hashed, the hash begins with a number of zero bits. This means that once you are able to find that value you get the transaction itself in reward, and the coins becomes yours.

### The algotihm

1. New transactions are broadcast to all nodes.
2. Each node collects new transactions into a block.
3. Each node works on finding a difficult proof-of-work for its block.
4. When a node finds a proof-of-work, it broadcasts the block to all nodes.
5. Nodes accept the block only if all transactions in it are valid and not already spent.
6. Nodes express their acceptance of the block by working on creating the next block in the chain, using the hash of the accepted block as the previous hash.

If two nodes propose the block at the same time what happens is that the one that is in the longest chain is considered the correct one. This means that nodes start working on one of the two but also keep the other one available in case it actually becomes the one with the longer chain.

Once the latest transaction in a coin is buried under enough blocks, the spent transactions before it can be discarded to save disk space. To facilitate this without breaking the block's hash, transactions are hashed in a Merkle Tree with only the root included in the block's hash. Old blocks can then be compacted by stubbing off branches of the tree. The interior hashes do not need to be stored.

### Issue with this technique

There is only 1 block added every 10 minutes. Also each block only contains 1MB of data so the performance is really poor. To mine a block it's needed more than the energy required in a US house in 1 year.

Also if 1 node owns more than 51% of the chain work, it can mine what it wants. Fortunately it's impossible for this condition to happen realistically in real life.

A variant is the **Ethereum** with it's pros and cons.

## POS

**Pos** is a different algorithm that doesn't require mining. It's **permissionless** and it works by picking a random person to assign a validator every 10 seconds. The block is linked to his father and normally this converges in a single chain.

This algorithm has pros and cons (**See slides for more details**)

## POX

There are many different algorithms that can be used in blockchain. All of them usually need a user to have a proof of something. Some examples:

- Proof of deposit
- Proof of coin age
- Proof of coin age
- Proof of identity
- Proof of elapsed time (I don't give proof of work but I give proof of have waited a enough time. This doesn't need any kind of high power. The main issue is that the TEE is something hardware so if someone is able to tamper with them they can access many more contracts than they should)

### PBFT Practical Byzantine Fault Tolerance

Basics:

- It’s the first algorithm based on BFT used in blockchain
- It’s based on deterministic replicas of a server: if they don’t fail, they generate the same result.
- If f replicas fail, the algorithm works with n=3f+1 nodes

Concepts:

- Client nodes send transaction requests
- The protocol works with the primary backup approach
  - Replica nodes are responsible for finalizing blocks. They move in different configurations (changed each round) called views
  - Each view has one primary replica (creates blocks, finalizes blocks) and backup replicas (finalize blocks)
  - The primary chooses the execution order from the client's requests

**More in-depth in the slides**

*Comparison of different algorithms:*  
![Comparison of different algorithms](../Screenshots/POX)

## Smart contracts

They are self-executing contracts with the terms of the agreement between buyer and seller being directly written into lines of code. The code and the agreements contained therein exist across a distributed, decentralized blockchain network.

The point is that if I put my code in the blockchain in a correct way I can make it self-executing. *I.e:* NFT, non-fungible tokens.

They are widely used in gaming, art, music and also in real state.
