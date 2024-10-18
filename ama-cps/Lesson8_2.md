# Distributed commit

## Two-phase commit protocol

In this protocol we assume the absence of failure (but still nodes unable to actually commit). It is made out of two phases:

- **Phase 1:** the coordinator sends a prepare message to all the participants. The participants answer with a vote (yes or no) and they are not allowed to commit until they receive a commit message from the coordinator. If the coordinator sends an abort then everyone aborts.
- **Phase 2:** the coordinator sends a global commit message to all the participants. The participants can now commit. The coordinator sends such message only if all the votes are for commit.

**finite state machine:**  
![2PC](../Screenshots/2PC_machine)

### Handling failures

In real life we must also think about failures. Let's think of an example:

- the participant is waiting in INIT state for VOTE-REQUEST from the coordinator
- the coordinator ended up in a WAIT state collecting votes
- another participant is blocked in READY.

In this scenario what we want is probably is the commit to be aborted cause it's an unattended state.

- the participant waiting in INIT state sends an ABORT once he reaches timeout.
- the coordinator sends a global ABORT after the timeout.
- the participant blocked in READY must find a way to recover the message that he previously missed.

### Failing participant

A participant is failed in state S and recovers to S

**Option 1:**

- **INIT:** he didn't know the protocol, no problem
- **READY:** he needs to know which state transition he should perform -> requires a log of the coordinator decision.
- **ABORT:** removes workspace results
- **COMMIT:** copies workspace contents

**Option 2:**
![2PC_recovery](../Screenshots/recovering_2)

### Failing coordinator

The coordinator could fail and not be available for a long time. What happens in that case?

An option is that the participant in WAIT state re-send a VOTE-REQUEST based on a timeout. The same for ABORT and COMMIT decision.

**Main issue:** this cannot work in asynchronous systems cause the concept of a timeout is non existent. So we consider a semi-asynchronous system.

## Kind of recovery

- **Forward recovery:** the system is able to recover from a failure and continue the execution from a new state
- **Backward recovery:** the system is able to recover from a failure and continue the execution from a previous state

In real life we usually use the second one by defining **recovery points**.

What really happens is that we can define checkpoints that are consistent among the whole system.

### Reaching a global consistent state

#### Coordinated checkpointing

Each process takes a checkpoint after a globally coordinated action:

- The coordinator sends a multicast
- The participants take a checkpoint and then send a message to the coordinator to confirm that they have taken the checkpoint
- The coordinator waits for all the confirmations and then sends a global checkpoint done message.

*Main issue:* the system must not have any other action between the checkpoint and the global checkpoint done message. This might not be feasible in a real world scenario.

#### Uncoordinated checkpointing

Each process takes a checkpoint when it wants but if it's done at the wrong time it might be needed to perform a **cascaded rollback** at system startup.

How cascaded rollback works:

- Let CP_i(m) denote the m^th checkpoint of process P_i INT_i(m) the interval between CP_i(m) and CP_i(m+1)
- P_i sends a message in interval INT_i(m) and piggybacks (i,m)
- When process Pj receives a message in interval INT j (n), it records the dependency INTi (m) -> INTj (n).
- The dependency INT i (m) -> INT j (n) is saved to storage when taking checkpoint CPj (n).

*Main issue:* this might be very expensive in terms of time and resources needed. To avoid that we usually implement **logging**

#### logging

The point of using logging is that we can assume that even if a process has non-deterministic behavior, in each of his state he is doing a determinated thing so by knowing the state sequence we can reproduce what he did.

**Notation:**

- **DEP(m):** processes to which m had been delivered. In addition if m*casually depends on m, and m* has been delivered to Q, then $Q \in DEP(m)$
- **COPY(m):** processes that have a copy of m but not (yet) reliably stored it
- **FAIL:** processes that have failed.

There are some schemas that can be used to implement logging:

- **Pessimistic logging:** for each nonstable message m, there is at most one process dependent on m (|DEP(m)| <= 1)

- **Optimistic logging:** for each nonstable message m, we ensure that if COPY(m) $\subseteq$ FAIL, then eventually DEP(m) $\subseteq$ FAIL.
