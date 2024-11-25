# Broadcast problem

## Assumptions

In this case with **assumptions** we mean **restriction**. We are not considering how to make this assumption be true, we just consider them true from now on:

- **Unique initiator**: there is only one entity that can start the broadcast
- **Total reliability**: the message is delivered to all the entities in the network
- **Bidirectional links**: the communication is bidirectional
- **G is connected:** the network is connected (*Note:* this is necessary cause otherwise the problem is straight up unsolvable)

## Flood

If an entity knows something, it sends the info to the neighbors. In this case we consider one entity as the **initiator** and the others as **sleeping**.

*Note:* check the slides for pseudo-code.

The algorithm is **correct** because it terminate in a finite time (follows from G being connected and total reliability)

### Message complexity

We consider m links, and 2 messages for each link (one for the request and one for the response). So we have $2m = O(m)$ messages.

**In total:** $\sum_{x}|N(x)| = 2m$. (Being more precise we have $2m - (n-1)$)

*Note:* the message complexity depends on the network topology.

### Example: labeled hypercube

In this case we have a hypercube with n nodes. The hypercube is a graph where each node has a label of n bits. Two nodes are connected if they differ by exactly one bit.

In this case we have $n = 2^k$ nodes and $k = \log_2(n)$ bits. The complexity of the algorithm is $O(n \log n)$. Not bad but we can do better

#### Hyperflooding

This algorithm represent an improvement of the previous one that works in a hypercube. The idea is to use the **label** of the nodes to avoid sending the message to the same node multiple times.

In this case the complexity becomes $O(n)$.

*Note:* look the slides for the last part with the proof.

## Spanning tree construction

A **spanning tree** T of a graph G is a tree that contains all the nodes of G. The tree is rooted in the initiator.

### Protocol SHOUT

This protocol is used to build a spanning tree. We start with a set of **Tree-neighbors(x)** that start empty, and that will contain all the edges of the spanning tree in the end.

The initiator sends a request to all the neighbors. When a node receives a request to be neighbor of someone it answers yes if it's the first time that it replies to such request, otherwise it says no.

Every node that receives a request to be neighbor of someone else understands automatically that he's not the root of the spanning tree.

If a node receives all the answers from the neighbors it goes into a **done** state.

The algorithm is correct and terminates in a finite time.

#### Message complexity

The messages sent in SHOUT are $2M(FLOOD)$. This is an upper bound, but gives a representation of the complexity of this protocol

*Note:* this means that it might be efficient to use SHOUT to create a spanning tree and then use algorithm that take advantage of the spanning tree created to do better than FLOOD in total.
