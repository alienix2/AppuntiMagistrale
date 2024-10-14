# Failure detectors

**Failure detector:** in this model we define a **distributed oracle** which provides indications on crashed processes. *Note:* in general an oracle could be wrong but we are not considering the actual implementation of the oracle and we are considering it as correct.

Each process can access a table that contains processes suspected to have failed. The table is contained in a module of the failure detector. This allows to have some kind of synchronization.  
The list is **NOT** static, a process could be wrong in evaluating the failure of a process and therefore a process' state could be changed back to running from failed. This means that two failure detector can have different tables at the same time, the more synchronization we involve, the more the failure detectors will be correct.

There are different classes of failure detectors, based on the following properties:

- **Completeness:** the failure detector must eventually detect every process that has failed.
- **Accuracy:** the failure detector must not suspect a process that is still running.

Completeness can be distinguished in:

- **Strong completeness:** each failed process sooner or later will be permanently suspended by all the correct processes
- **Weak completeness:** each failed process sooner or later will be permanently suspended by at least one correct process.

*Note:* the main problem of strong completeness is that a failure detector that always suspects all the processes is compliant to it.

- **Strong accuracy:** no correct process is suspected by any correct processes
- **Weak accuracy:** no correct process is suspected by at least one correct process.

- **Eventually strong accuracy:** there is a time after which correct processes are not suspected by any other correct process.
- **Eventually weak accuracy:** there is a time after which some correct processes are not suspected by any other correct process.

![completeness_accuracy](../Screenshots/completeness_accuracy)

It's possible to define a **reduction algorithm** that allow to reduce a failure detector to another one. This means that if we reduce a FD C to an FD D, we can say that all the problems that can be solved using D can also be solved using D.
![completeness_accuracy_reduction](../Screenshots/completeness_accuracy_reduction)
*Note:* we can avoid considering the creation of a FD like the one in the first row cause P≅Q.  
**Note:** see the slides for a formal demonstration of P≅Q

**Intuitive demonstration:** we have a failure detector that decides what's right and what's wrong I can easily implement a consensus algorithm. The basic Idea is that if a process fails there is an algorithm that can remove it and therefore allow the other processes to have consensus. I start by considering that there is such oracle.

## Algorithm for consensus

**The consensus problem can solved with a class S FD.** So in particular we are considering strong completeness and weak accuracy. The algorithm is made out f 3 phases:

1. **Phase 1:** each process proposes a value and sends it to all the other processes. Each process decides the value that has been proposed by the majority of the processes. All the processes are waiting for messages from all the other processes. The only exception to that is if they actually decide that one or more of the other processes actually failed.

2. **Phase 2:** consensus agreement, the processes agree on a vector based on the value that has been proposed by the majority of the processes.

3. **Phase 3:** the processes decides for the first non null value of it's copy of the vector V_p
