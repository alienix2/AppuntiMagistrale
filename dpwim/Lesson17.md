# Election problem and yo-yo protocol

## Election problem

We have a system in which all the nodes have the same configuration. We want to start from here and end in a configuration in which all the entities are in the same state **except for one** which is the **leader**.

### Impossibility result

We start from the standard restrictions (BL, CN, TR), and we have the following **proof**:

By contradiction:

- we consider a system with two entities, x and y, in the same initial state
- if P solves the problems, it works in any condition
- if we consider a synchronous scenario in which x and y start simultaneously they start doing the same thing
- if one becomes the leader, the other one should become the leader too

**We need to break the simmetry** to solve the problem. We give to each node a **unique identifier**

### Solution strategy

#### elect minimum

- find the smallest id
- the leader is the one with the smallest id

*Note:* finding the minimum among the nodes is the election process

#### elect minimum initiator

- find the smallest id among the initiators
- the leader is the one with the smallest id

#### elect root

- build a rooted spanning tree
- the leader is the root of the tree

### Yo-yo protocol

In this algorithm we have **no assumption on the topology** of the network. This is a **minimum finding algorithm** composed of two parts:

1. **Pre-processing phase**: each entity exchanges the id with all its neighbors, then x orients its links in the direction of the entity with the biggest ID. This creates a **DAG** (directed acyclic graph) (*Note:* this is clear if we look at how the graph is created). We can define a **Sink** and a **Source**, which are nodes that doesn't have arcs coming out and coming in respectively.
2. **Sequence of iterations**: in each iteration there is a stage in which some candidates are "defeated" and don't continue to the next stage. This phase is divided into two parts:
    1. **Yo**: in this step each source sends it's id to the neighbors. The internal nodes compare all the IDs from it's neighbors, compute the minimum and then sends it to all it's out-neighbors. A sink waits until it receives all the values from it's neighbors and then proceeds to the second step of the process
    2. **-Yo**: in this step each sink answer YES to all the in-neighbors that sent the smallest value. An internal node waits until it receives the vote from all the out-neighbors, if all the votes are YES it sends YES, otherwise NO. A source waits until it receives the votes from all its in-neighbors, if all votes are YES, it survives and goes to the next iteration.

This represents one iteration, but the process to compute the leader needs more iterations, in particular after 1 iteration we need to flip the links where a NO vote was sent, which means that any source that received a NO will become a sink.

How can a node understand that he is the leader? We will need to perform **pruning**, which will make it so that at the end the leader will be the only node alive.

#### Pruning

Pruning is performed using two rules:

- if a sink is a leaf then it's useless and can be pruned
- is node in the yo step receives the same value from many neighbors, it can ask all of them, except one to prune the links

*Note:* pruning is performed during the voting phase

#### Complexity

**without pruning:** there are 2 messages for each link at each phase so if we consider the number of phases as log(# sources) we have **TOT**=m + 2mlog(s)
**with pruning:** we have a complexity that should be lower than the above (it cannot be higher)

## Election in dynamic network

In this case a thing to consider is that the network is not static, so we need to consider the **topology changes**. They might happen cause new nodes enter the net or because a node of the network fails.

### Bully algorithm

#### Assumptions

- The system is **synchronous**
- the entities may **fail at any time** including during the execution of the algorithm
- there is a **failure detector** that can detect the failure of a node
- message delivery is reliable
- the topology is a **complete graph** and each entity knows it's ID

#### Messages

There are 3 kinds of messages:

- **Election** sent to announce an election
- **Answer** sent to answer to an election message (to know that a node is alive)
- **Coordinator** sent by the leader to notify the victory

#### The algorithm

An entity starts the protocol (there could be many initiators) when the current coordinator failed or it has just restarted and needs to recover

1. If x has the highest ID, it sends a coordinator message to all the other entities
2. If x doesn't have the highest ID, it sends an election message to all the entities with a higher ID
3. If x receives no message after a certain time, it sends a coordinator message to all the other entities
4. If x receives an election message from a node with a higher ID, it sends an answer message to that node
5. If there is no notification after a certain time, x restarts the election
6. If x receives an election message from another entity with a lower ID, it sends an answer message to that entity and then restarts the election
7. If x receives a notification from another entity, it treats that entity as the coordinator

#### Complexity

In the worst case scenario we have:
$$\sum_{i=1}^{n-1}i = \frac{n(n-1)}{2} = O(n^2)$$

## Election in wireless environments

In this case not only the network is dynamic, but also the topology is dynamic and might change over time. Also the message-passing is not reliable and entities **don't know** the topology of the whole network.

An **ad-hoc mobile wireless network** is a network in which the entities are mobile and can communicate with each other without the need of a fixed infrastructure. They have some **pros**: they are easy to deploy, they are cheap, they are flexible. But they also have some **cons**: they are not reliable, they have a limited bandwidth, they have a limited range.

### Leader election

We consider a network of entities with a value and a **finite number** of topological changes. And we want to have all the nodes selecting a single leader (the node with the highest value).

#### The algorithm

The leader sends periodically an **heartbeat** to the other nodes. If a node doesn't receive the heartbeat for a certain time, it starts an election.

The basic schema considers a **single initiator** and **no failures**:

1. The initiator starts building a SPT
2. leaves start a convergecast computing the leader
3. the root of the SPT notify the leader to all entities

There are 3 kind of messages:

- **Election** sent to announce an election
- **Ack** to join the spanning tree and carry info about a candidate
- **Leader** to notify the leader

#### Handling concurrent computation

We need to add some rules to handle the case in which multiple entities start the election at the same time:

- A node can take part only in one election process
- There is a computation-index that identifies the computations and they are totally ordered
- If a node receives an election message with a higher computation-index, it stops the current computation and starts the new one

#### Node partition

If the network is partitioned, we need to consider the case in which the leader is in the partition that has the majority of the nodes. In this case the leader will be the one that has the highest value.

*Note:* we need to identify the node disconnection

#### Merge partitions

When there is a merge we just pick the leader with the higher value if a leader is elected in both the partitions. Otherwise if one is still performing the process, we let that partition finish the process and then we pick the leader with the highest value.
