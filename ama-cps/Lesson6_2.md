# Distributed coordination

This part is already treated in the course DPWIM.
Arguments treated:

- **Event-ordering**: the order of the events is important in a distributed system. This is because the events can be concurrent and the order of the events can change the final result.
- **Mutual exclusion**
- **Atomicity**
- **Concurrency control**
- **Deadlock**
- **Election algorithms**
- The final goal **Reaching agreement** **(consensus)**

## Event-ordering

This part is based on timestamps. As we discussed already usually each machine as its own internal clock. There is no basic notion of global physical time. The oscillator on different machine will naturally become out of sync as time passes. Finding a way to synchronize all the clocks if fundamental.  
*I.e:* if we think about the make utility, to understand if something has to be recompiled the utility uses a time-stamp in order to understand if something is new or old.

**Logical clocks** are used to order events in a distributed system. The logical clocks are not based on the physical time but on the order of the events. This is useful to define a relative order of event. When we think about logical clocks they must be created so that a full order is defined, partial ordering is not sufficient.

**Some basic rules:**

- The ordering within a specific process can be easily defined by the single process.
- When a message is sent the event of sending happens before the even of receiving.
- If a->b this means that a affected b. The two events are **casually related**. There might be cases in which two events are not related.

If there is no relation the physical time cannot help us either, cause of the different clocks. In this case we need to introduce a **logical clock**.

**Logical clock:**  
a logical clock is a software counter that is incremented each time an event happens. This logical clock is used to assign a time-stamp to each event.  
How they work in practice:  

- CP_i := CP_i + 1  
- When a message is sent the time-stamp is attached to the message. When the message is received the time-stamp is updated and assigned to max{CP_j, tm}.
- The new value of CP_j is used to time-stamp the event of receiving m by P_j.

*Note:* these 3 rules are only defining **partial order** cause events on different nodes might have partial order. So **total order** and **causal order** are not well defined.  

### Defining total order

To define a **total order** I can identify a **global logical time-stamp**. This is done by defining a time-stamp as a couple. The process P_i has it's time-stamp in the moment a defined with (CP_i(a), i). In this way we can first look at CP_i(a) and then if they are the same, the total can be determined by looking at i and j, if i>j, i happened first.  
*Note:* this still doesn't define causal order, but it defines a total order. But there are cases in which it's not needed, for instance if we talk about transaction, they are always independent one from the other, so total order is enough.

### Defining causal order

To define the **causal order** we need to define **vector clocks**. This is a vector of logical clocks, one for each process. The vector is updated each time an event happens. The vector is updated in the following way:
The value of CvPi is used to assign timestamps to events in process
Pi. CvPi (a) is the timestamp of event a in process Pi:

- CvPi [i], the i-th entry of CvPi,corresponds to Pi’s own logical 10:30
- CvPi [j], j ≠ i, is Pi’s "best guess" of the logical time atP

*Example*
![Vector clock](../Screenshots/example_vector_clocks)

## Synchronous and asynchronous systems

Distributed systems can be classified according to specific characteristics:

- **Synchrony degree**
- **Type of failure**
- **Network topology** (and many more...)

### Synchronous systems

A system is defined as synchronous if:

- there exist an upper bound on message delivery
- the drift rate of the local clock of each processor w.r.t the global clock is bounded
- there is an upper bound on the processing speed of each processor.

### asynchronous systems

An asynchronous system is a system that doesn't have a limit **EITHER** on message delivery delay **OR** on the local clocks drift **OR** on the speed of each processor. Basically in an asynchronous system, we cannot make any assumption on the time (**time-free**).  
We note very easily that it's easier for a system like this to work but at the same time it's also easier for a failure to happen. We can make specific assumption on the system and work in a probabilistic way.

*Note:* the two models presented are at the opposites of a continuum, there are techniques that are in between the two.

In an asynchronous system is impossible to distinguish if there is a crash or if the message is lost or if the network is failing or the node is under heavy load and therefore very slow.

## Distributed consensus

The goal of distributed consensus is to reach an agreement among a group of processes. The agreement is reached when all the processes agree on a specific value. The agreement is reached if the following conditions are met:

- **Termination:** all the correct processes eventually decide on a value.
- **Uniform integrity:** all the correct processes decide at most only one time.
- **Agreement:** all the correct processes decide on the same value.
- **Validity:** if a process decides on a value, this value was proposed by some process.

*Example:* I consider an unreliable broadcast where the communication suddenly fails. I have all the above except for termination cause a failed process won't be able to agree with the others on a value.

In reality we consider the rules a little bit more relaxed, in order to create a protocol that works IRL.

### Example of a protocol

- **Asynchronous system**
- **Process fail by crashing:** the process stops working and doesn't send any message anymore. (don't consider Byzantine failures)
- **Correct/Faulty process:** a process is correct if it doesn't fail, otherwise it's faulty.

We are creating a Best-effort broadcast algorithm, so we consider:

- **Validity:** if p and q are correct, then every message B-broadcast by p is eventually B-delivered by q.
- **Uniform integrity:** no message is B-delivered more than once.

**Problem:** if the sender crashed before sending the message, the message will never be delivered but this will always be compliant with the protocol above.
