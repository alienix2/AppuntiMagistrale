# More on synchronization

## Distributed Mutual exclusion

I consider a system with n entities and 1 shared resource. I want to entities to access the resource one at a time.

Usually in multi-threaded programming, we use locks to achieve mutual exclusion. There are also other solutions like semaphores or monitors. The issue is that in this case we have no concept of shared memory to implement them.

We want to be able to guarantee the following properties:

- **Mutual exclusion**: At most one entity can access the resource at a time.
- **Fairness**: No entity waits forever to access the resource.

There are two kind of algorithms to achieve mutual exclusion in distributed systems:

- **Token-based algorithms**: A token is passed around the system. Only the entity holding the token can access the resource. *Note:* the main clear issue is what happens if the token gets lost
- **Permission-based algorithms**: An entity must ask permission to access the resource.

### Centralized algorithm (token-based)

The basic idea is having a special node in the system called **manager** that grants permission to access the resources. Any entity that want to access a resource in the system must ask the leader for permission, when the leader answers, the entity can access the resource

#### Message complexity

In general to access a resource we need the following steps:

- a request from x to the leader
- a response from the leader to x
- a message of the entity to the leader for releasing the resource

So we can say that: $3d(x, r) < 3diam(G)$

In a complete network this means that we only need 3 messages, but in other kind of network the cost becomes a lot higher.

**Pros:** is correct and fair, few messages are required (in the best scenario)
**Cons:** the leader is a single point of failure, the leader can be a bottleneck, the leader can be a target of attacks

### Traversal-based algorithm (token-based)

In this case we consider a special message that we identify as a **token** in our network. The token traverses the network and each entity needs to have the token in order to access the resource it's connected to.

*Note:* if x needs to access the resource it will use token, otherwise it will just pass it over to someone who needs to access it.

#### Concrete implementation

There are multiple algorithm used to implement traversal:

- DF, DF+, DF++. The cost is usually O(m) (m number of edges)
- using a spanning tree. O(m) for building it and O(n) for traversing it (m number of edges, n number of nodes)

**Pros:** is correct and fair, starvation cannot occur
**Cons:** the token can be lost. *Note:* also the basic topology that allows to implement this kind of algorithm (ring network) is not really robust cause if a malicious node is present it may block all the others from receiving the token. Also in case of a failure, the token might disappear from the net.

### AskAll algorithm (permission-based)

In this case we consider that an entity needs to ask permission to all the other entities in the network to access the resource. If all the entities agree, the entity can access the resource. *Note:* this requires a total order of all the events in the system (usually uses the Lamport clocks)

#### Concrete implementation

x sends a message to all the other entities in the network containing the request and it's logical clock. When y receive a request it should:

- if it doesn't need the resource, it sends an OK message to x
- if it's using the resource, it will enqueue the request
- if it has requested the resource, it compares the logical clock and the one in the message. If the message is older, it sends a message to x with an OK otherwise it will enqueue the message

*Note:* when a message is enqueued, nothing will be sent back to x. This is because in this way x will wait for the OK until it's his turn to access the resource.

#### Message complexity

For a request we need:

- n-1 request messages
- n-1 OK messages

So we can say that: $O(n) = 2(n-1) = 2n - 2$ (n number of requests)

**Pros:** is correct and fair, starvation and deadlock cannot occur
**Cons:** if a node fails, the system will be blocked. We need multicast primitives. If a node has small capabilities it might be hard for it to obtain the access to a resource.

### Quorum-based algorithm (permission-based)

This algorithm uses a voting schema. This means that an entity needs to ask permission to a subset of the entities in the network. If the majority of the entities agree, the entity can access the resource.

In this case we assume:

- the entities are replicated n times
- each replica has a coordinator
- when a node wants to access a resource, it must obtain the permission from the majority of coordinators ($m>\frac{n}{2}$)

#### Message complexity

In this case we consider **m** number of coordinators. We consider x an entity wanting to access a resource R.

x needs to send m messages and it receives m messages at most, which means that in total the number of messages is below 2m.

*Variant:* we consider that if x isn't granted the permission it will send all the messages again. In this case we have at most 2mk messages (k number of retries needed).

*Note:* in this algorithm a node can access a replica with a coordinator that said yes to, but it can't access a replica with a coordinator that said no.
