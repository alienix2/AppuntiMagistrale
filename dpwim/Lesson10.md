# Block-chain architecture

In this case we are talking about a system that allows the registration of transactions into distributed ledgers.

In this case we are thinking of a P2P network in which the nodes doesn't trust each-other. The system is usually organized into three layers:

- **Network layer:** the layer that represents the p2p network representing the participants
- **Consensus layer:** the layer that represents the rules that are used to validate the transactions
- **Application layer:** the layer that represents the application that is built on top of the blockchain (*I.e:* a smart-contract)

When a transaction is ready a node must decide to communicate it to the other ledgers. The **validators** (sometimes referred as **miners**) validate them, group them in a block that is appended to the ledger and then propagate the blocks to the others in the network.

There must be a way to understand who is allowed to add blocks to the network. This means that the peers must all achieve consensus using an alone algorithm. The most famous algorithm is the **Proof of Work** algorithm.

The two options are:

- a small selected group is identified as a trust-third party
- the consensus is achieved through the use of a distributed algorithm that is based on the idea that the majority of the nodes are honest.

## Kinds of block-chain

- **Permissionless:** the blockchain is open to everyone. *I.e:* Bitcoin
- **Permissioned:** the blockchain is open only to a specific group of people. *I.e:* Hyperledger

## A case study of a P2P system: Bitcoin

The idea of analyzing this case study is to understand how all the theory we discussed can be implemented in real life.

*Note:* this is also discussed in [Lesson_10 of the AMA-CPS course](../ama-cps/Lesson10.md)

The basic Satoshi Nakamoto's idea was to create a system that allows the exchange of money without the need of a central authority. The system is based on the idea of a **blockchain**.

### Cryptographic Ingredients

**Hash function:** an has function is a mathematical function that takes an input and returns a fixed-size string of bytes. The hash function must have the following basic properties:

- **Efficient**
- **Probability** of generating a hash value should be around the same for all the possible values

**Other properties:**

- **Collision free:** *Note:* in general the hash function is not injective, so there can be multiple inputs that generate the same output. This is called a **collision**. A function that is completely collision free doesn't exist, but we can think of functions that make it so it's not feasible to find those collisions. This means that the hash of a specific data can be used to identify that piece of data. *Note:* again, that's not a mathematical property, is just that we assume that it's impossible to have a collision in real life.

- **Hiding:** the hash function should be hiding. This means that if we have a hash value we cannot understand what the input was. This is usually achieved by using a **salt**. The salt is a random value that is added to the input before hashing it. This means that if we have the hash value we cannot understand what the input was unless we know the salt. This is also a must of the starting set is made out of a low number of elements.

- **Game friendly:** the hash function should be game friendly.

#### Proof of work

The idea of the proof of work is to find a value that when hashed the hash begins with a number of zero bits. This means that once you are able to find that value you get the transaction itself in reward, and the coins becomes yours.

The idea came from solving a problem about spam emails. The idea was to make the sender of the email do some work before sending the email (solve a **challenge**). This way the spammer would have to do a lot of work to send a lot of emails.

### Digital signature

A digital signature is used to identify users and verify the integrity of the data.

We use a **private key** to encrypt the data and a **public key** to decrypt it. This means that the public key can be shared with everyone, while the private key must be kept secret.

Anyone can verify if the data was signed by the owner of the private key by using the public key but none can fake being the owner if they don't have the secret key.

## Bitcoin components

### Transaction

A basic of bitcoins is the **transaction**. A transaction has:

- an ID
- a list of inputs (if you want to spend money you need to have a previous transaction that gives you the money, otherwise there is no need for input)
- a list of outputs (the money that you want to be created)

*Note:* it actually happens that the system forge the money, in which case the transaction won't have any list of input.

### System

Bitcoin is entirely P2P, this means that there is no central authority. In the network anyone can operate as a **miner** or as a **client**. The miners need to validate the transactions and therefore run the consensus algorithm to decide which block can be appended to the end of the block-chain. The basic idea is that the miner want to extend the longest block-chain.

When a new transaction is created it's broadcasted to all the nodes. All the nodes collects all the new transaction into a block and the run a consensus algorithm so that all the nodes can agree on the next block to add to the block-chain. This means that the next block will be created starting from the hash of the chosen block.

#### Consensus algorithm

The idea behind a consensus algorithm is that:

- it must terminate with all honest nodes agreeing on the same value
- the chosen value must be proposed by an honest node

In general it's **impossible** to achieve that in a distributed system.

In **Bitcoin** we use a consensus algorithm that is based on the idea of the **Proof of Work**. The idea is that the miners must find a value that when hashed the hash begins with a number of zero bits. The difficulty of the puzzle is adjusted so that a new block is appended every 10 minutes.

The miners have incentives to behave honestly and mine new blocks:

- they get a reward for mining a new block, which is the possibility to create new bitcoins
- they get **transaction fees** for the transactions that are included in the block they mined. The transaction fees are the difference between the sum of the inputs and the sum of the outputs.

#### Block-chain forks

It may happen that two miners solve the problem at the same time (or with a difference in time so little that they cannot know that another miner already mined the block before him).

This means that we might have two versions of a block-chain, but that's not an issue cause everyone agrees to the longest version of the block-chain. The transaction in the other block will be "re-inserted" in another new block later.

*Note:* a block in the block-chain is called **stable** if it has 6 blocks appended after it, this means that it's very unlikely at that point that the block-chain containing that block will be the one discarded. This is one of the main issue in Bitcoin cause it takes a lot of time to make a transaction stable and sometimes this is not acceptable in real life scenarios.

## Bitcoin limitations

- **scalability:** the system is not scalable, the number of transactions that can be made is limited
- **privacy:** the system is not private, all the transactions are public, this means that someone can trace if specific wallets are used for certain kind of operations
- **energy consumption:** the system consumes a lot of energy

## Other block-chain systems

- **Ethereum:** a system that allows the creation of smart-contracts. The idea is having a distributed infrastructure, in which every component has some code.
- **Hyperledger:** a system that is permissioned, this means that only a specific group of people can access the system. The idea is to have a system that is more efficient and that can be used in a business environment.
- **Moner:** a system that is more private than Bitcoin
- **Cardano:** a system that is more scalable than Bitcoin

### Ethereum and smart-contracts

The concept of **smart-contracts** was introduced way before the introduction of Ethereum. The idea is to have a contract that is self-executing and that is stored in the blockchain. The contract is executed when a specific condition is met.

## Attacks on Bitcoin

**Check the slides for the attacks** they weren't discussed in the lecture.
*Note:* the professor is working on block-chain right now so it's a good topic for a thesis with him.
