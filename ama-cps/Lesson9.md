# Timed asynchronous systems

One of the things to consider is that in reality clocks exist and a human knows the passing of time. *I.e.* If I browse the net and the page it too slow I try to refresh it or I close it.

In this model we make assumptions on the behavior of processes, communication and HW clocks:

- all services are times. So they can define time-outs
- communication is done through datagrams (non reliable)
- processes are subject to crash or timing failures (**NO** byzantine failures)
- processes can access local clocks that have limited clock drift
- there is no limit to the failure rate of the processes (so they are "normal" and must be anticipated in our model)

*Note:* we assume that the clock drift is bounded by a certain value. So in any moment the drift is within [-p, p] but it doesn't have to be constant, just within the limit

## Datagram service

- Unicast and broadcast
- messages are univocally determined
- no upper bound in the delay
- there is a time-out in message transimission
- time is proportional to dimensions of the message
- only omission and timing failures (cause corrupt messages aren't considered probable)
- process can have crash and timing failure

*Note:* usually we consider the time-out so that we can ignore the scheduling delays.

**Processes states:**

- **Up:** the process is working correctly
- **Crashed:** the process is not working
- **Recovering:** the process is recovering from a crash

We use hardware clock but we suppose that there is **drift bound**. Clocks **can crash** and this causes also the crash of the whole process usually (the opposite is usually not the case).

### Stability predicates

In the specifications of the protocols defined for timedasynchronous systems, we often resort to the use of stability predicates that verify system favorable conditions.
**Stable** -> behaves like a synchronous system
We need to introduce a definition:

- Two processes are connected in the time interval [s, t] if they are timely in [s, t] and every message exchanged suffers a maximum delay of δ (one-way time-out delay).
- If the majority S of the processes are pairwise connected in an interval [s, t] we say that S is a **stable majority**.

A system is defined as **majority-stable** in an interval if a stable majority exists. Also a process is **majority-stable** in an interval if it is connected to a stable majority in the interval.

A system is **always eventually majority stable** if:

- after each instability period the system eventually becomes majority stable for atleast $\delta$ time units
- each process eventually becomes majority stable for atleast $\delta$ time units (or suffers from a crash)

### Termination conditions

In the case of timed asynchronous systems, we talk of conditionally-timed conditions in a system which is always eventually majority stable, if a process p is majority stable in an interval [t, t+E], then an operation initiated at instant t must terminate by t + E

### Progress assumptions

These assumptions allow to solve problems like **consensus**. The assumptions can be summarized as:

- **Infinitely often** a majority of the processes will be stable for a limited interval.

The point is that with this assumption if a system is stable then it's able to procede with it's computation in a finite time. Which basically means that **when a system is stable it behaves exactly as if it was a synchronous systems**.

*Example: rotating leadership:*  
Assumptions:

1. at any time instant there exists at most one Leader
2. only a majority-stable process is elected as leader
3. a process remains leader for a limited time
4. a process knows that it is a leader (it is not required that other
processes know who the leader is)
5. the clocks of the processes are synchronized (the deviation
between the clocks is limited by some constant)

The second assumption formally means:

2. if a system is majority stable in an interval [t, t + E] then there will be a leader always selected and each process will eventually be the leader.

Also with the fifth assumption we can make sure that in each moment there is only one leader, even if the clocks aren't perfectly aligned.

The algorithm:

- At the beginning of each time-slot, each process is a candidate to be elected leader.
- Each process is associated with a priority and the election protocol ensures that only the highest priority process is elected.
- For a process to become a leader, however, it needs to receive a majority of replies to its candidacy and that these replies come in time.
- After sending its application, in fact, each process waits for a certain period of time to receive the candidacies of the other processes before responding to the application with the highest priority.
- After becoming the leader, a process remains as such for LD clock-time units, after which it is "dismissed".

*Note:* one of the main reason why this works is that since we have a bounded drift, we can create a real-time envelop.

- When a process becomes the leader it performs a broadcast to know if the other processes know about the decision and about the previous proposals.
- The current leader waits (for 2 δ clock-time units) to receive replies after which:
  - if it learns that a process has already decided for w, then he too will decide for w and inform all the other processes via broadcast
  - if none of the processes from which it receives an answer is aware of a previous proposal, then proposes its initial value, otherwise it proposes the previously proposed value
  - if he does not know of any decision or does not receive a sufficient number of answers, he will not take any action

- Each process p that receives a proposal with an upper limit on the transmission delay at most Λ (maximum error allowed by the clock synchronization algorithm) and with a higher priority than the last proposal, stores the value and the priority of the proposal and responds to the leader by sending an ack to confirm the reception
- On the other hand, when p receives the leader's decision, he too decides for that value
- For both the leader, and for any other process that is in the restarting state, the receipt of a decision or of a timely proposal of a value determines the transition to the UP state
- A majority of processes know the proposed value v when the leader decides
for it.
- A process p that performs restart must re-initialize its protocol state before moving to the UP state.

*Note:* In this way the invariant is respected even when some process that knows the proposed value is "replaced" by other processes after having suffered a crash.
