# Other algorithms for consensus

## Flooding based consensus

**First consideration:** Nonfaulty group members need to reach consensus on which command to execute next

**Flooding based consensus:**

- a process group P = {p1, p2, ..., pn} is a set of processes
- fail-stop failure semantics
- a client contacts a process in P to propose a command
- every process in P maintains a list of proposed commands

**Consensus:**

- in round, every process in P multicasts its list of proposed commands to all other processes in P
- at the end of the round every process in P has a list of proposed commands from all other processes in P and merges them
- the next command is selected through a deterministic function known to all processes.

*Main issue:* processes cannot know if someone else received the same information he did if another process failed. -> **solution:** if the coordinator detects that another process failed the whole round is skipped

*Note:* another algorithm used is the **Paxos algorithm** which is a more complex version of the flooding based consensus but we're not going to cover that in the course (is on the book)

## Byzantine Consensus

The main problem of the previous algorithms is that they are not able to handle Byzantine failures. This name comes from the way Byzantine generals handled the troupes. They put different groups of army around the attacked army and all of them follow the same rules and attack in the same way after deciding what to do together. The main problem is that some of the generals that are deciding for their group might be traitors.

**What might happen:**

- The general of the whole army is indeed a traitor and he is sending the wrong message to the others.
- Another one of the generals is a traitor and is sending the wrong message using flooding. (But this could be easily solvable by considering the general as the one to always follow)

![byzantine](../Screenshots/byzantine_consensus)
This problem is not solvable with the previous algorithms.

**How many do I need to tolerate n traitors?** 3n + 1
*Example with a commanding traitor and 4 total generals:*
![byzantine_example](../Screenshots/byzantine_3n1)
The basic idea is that we pick a default value as retreat and therefore if majority is not reached the will all retreat.

At first this problem was considered interesting to study but irrelevant in the real world. This was until actual attacks to the security of a system started happening.

Nowadays this problem is also easy solvable by using a digital signature that allows to know if the commander is a traitor or not.

## Consistency, Availability, Partition Tolerance

**CAP theorem:** in a distributed system you can have at most 2 of the following 3 properties:

- **Consistency:** all nodes see the same data at the same time
- **Availability:** a guarantee that every request receives a response about whether it was successful or failed
- **Partition Tolerance:** the system continues to operate despite arbitrary message loss or failure of part of the system

**How can we understand this intuitively:**  
we consider a system with two processes that can no longer communicate cause the network failed. The **consistency** is violated cause A can still receive but cannot communicate the changes to B. **if** i decide to drop all the communications to A then i lose **availability**, **if** I decided to assume that they can always communicate correctly, **partitioning** must be violated.

This basically reduces to:
**CAP theorem is about a trade-off between liveness and safety**.  
The point is that if we have partitioning and we cannot guarantee consistency, how can we still guarantee consensus? We can assume to have an **eventual consistency** using some kind of cold recovery.
