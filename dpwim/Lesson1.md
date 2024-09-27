Starting with definitions of distributed-systems.

*First example:*
Data centers (Google): https://www.google.com/about/datacenters/ (Looking at the picture we see the challenges of modern distributed-systems). We will focus on the software side but there is many more to them.
We must think about our application independently from the location where it is going to be used. We don't want the programmer to care about many details of the hardware and environment.

*Second example:*
Every service (almost) on the internet. Most web-apps run on an hardware located in data-centers. Gmail is owned by google you don't know where your mails are located in particular. Usually there is redundancy.
A **content delivery network** is a distributed-system where the informations are stored in more than one place to allow the user to have the resource reachable faster.

*Third example:*
Bitcoins. From our perspective they are basically a distributed-system. There is a peer to peer system that allows us to use the blockchain. (More on this later on)

*Other examples:* modern cars, health-care system, telemedicine, smart cities, smart factories, smart agriculture.

**The challenge:** here the point is to make it so everyone is able to interact in a smart way. Everyone, and every device must share the same 'language'.

**Distributed-system:** is a networked computer system in which processes and resources are sufficiently spread across multiple computers.

Concept of a node, a system is a set of nodes.
We program the node so that they can interact to achieve a common goal. Nodes communicate through messages. Every node has it's own notion of time (which means that there is no global clock, each has it's own clock so they cannot synchronize through time).

**Main characteristics:**
Each node is a **computing element**. With multiple nodes communicating we create an **overlay network**. There are two approaches:
- Any node can join the network (dynamic). 
- Specific mechanisms are needed so that nodes can join and authenticate in the network.
**Overlay Network** and **Physhical networks** are different from each-other. The overlay network is built upon another network, like the physical one.
There are two types of overlay networks:
- Structured overlay network (tree, ring, hypercube)
- Unstructured overlay network

The system must appear as a **single coherent system** to the final user. There are information hidden to the user. For example if use Gmail I don't want to know where the data is or how it is being processed. Also the user doesn't need to know if there is any kind of redundancy.
This is very hard to achieve in real life. The quality of a distributed-system is related to how well it can be seen as a single unit.
Main problems in this regard are the possible **partial failures** and partial **inconsistent states**.

