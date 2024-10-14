# Synchronous and asynchronous systems synchronizThe previous algorithm implements RB

Continuing from the previous lesson, going more in depth with the examples.
![example_hard](../Screenshots/specific_execution_reliable)
In this example the communication still respects the protocol that we discussed before.

**Reliable Broadcast algorithm for synchronous systems**:

- Use of the message diffusion principle: when a process receives the message for the first time, it gets forwarded to all the other processes and then performs R-delivery.
- This algorithm satisfies the properties of the reliable broadcast protocol.

The algorithm implements reliable broadcast:

- Validity: if a process delivers a message m, then m was previously broadcast by some process.
- Uniform integrity: a process delivers a message at most once and only if it was previously broadcast.
- Agreement: if a process delivers a message m, then all correct processes eventually deliver m.

**Real case scenario:** people working on the railways tracks. We can think of having a Main coordinator and then people communicating to avoid getting passed on by the train. The information must be delivered so reliable broadcast must be delivered. The point here is that we need the messages to be delivered in a specific period of time so it's a **real time system**.

**Variants of reliable broadcast:**  

- **FIFO Broadcast:** the messages are delivered in the same order they are sent
- **Causal Broadcast:** the delivery order follows causality relationship
- **Atomic Broadcast:** the messages are delivered in Total order

![orders](../Screenshots/orders)

It's easy to prove that Consensus can be reduces to Atomic Broadcast:

- When a process wants to propose a value, it broadcasts it
- When a process wants to decide, it waits for the Atomic Broadcast to deliver the value

The point is that the FLP theorem, proves that it's impossible to solve consensus in an asynchronous system using atomic broadcast. Even if it's possible using the other types of broadcast.  
This is rather easy to see, what happens if one node fails? In this definition the other nodes don't know if they should just ignore the other node and proceed like he has failed. (But it could just be very slow). We cannot distinguish between a failed process and a very slow one.  
*Note:* Many models have been proposed to solve this problem, in particular we will see: **Failure detectors**, **Paxos**, **Timed-asynchronous systems**  
*Note:* In the last case we consider that the systems are synchronous only at specific times

## Review from this and the previous lesson

**Causal events:** this represents the fact that events are related to each other. What one does depends on the other event. There can be indirect casual relationships but there are many cases in which two events are completely unrelated.  
**Total order:** this happens when all the processes agree on the same order. It doesn't have to be a specific order, the point is that all the process know it and use it.
**FIFO-order:** this relates only to a single process. Each process has it's own order.  
If the last two ordering are respected we can define a **FIFO total ordering**.  
*Note:* in causal order there are many cases in which if we don't add **total ordering** we don't know which of many combination the process actually choose to follow.
