# Basic and recap on Distributed Systems

The first part is similar to the first part of dpwin. Check the slides.
*Example:* mining a bitcoin. We see how every computing element is alone and they all work together for single purpose.

There is no concept of a *global clock*. For instance if you have a wrong which is set wrong you can't go online.
For synchronization you must have a way to make the clocks communicate with eachother. The most common approach.

There is two types of Overlay network:
- **Structured**
- **Unstructured**

Hiding partial failures is an important part for a distributed system. A failure is an anomaly, we must build our system so that a failure is tollerated.
Each of the nodes of a distributed system must install an **OS** that gives a structure to manage the communication between them.

An example of a distribution **trasparency** is something like *inet_ntoa()* in C. It guarantess that all the users use the same protocol to communicate online.
**Types of distribution transparency:**
- Access
- Location
- Relocation
- Migration
- Replication
- Concurrency
- Failure

**Openness of distributed systems**
All the open systems should be able to communicate with other open systems. All the system should use a well-defined **interface** but they should also be able to **interoperate** and communicate.

Distributed systems should be **scalable**. Actually modern solutions doesn't really have a problem for scalability. There are only few problems that still need solving in this regard:
- **geographical** scalability (communication between distant countries is less reliable and more time demanding);
- **administrative** scalability (different laws for different countries).

# Types of distributed Systems

**Parallel computing:**
High performances obtainable by using multiple CPU to work on the same problem. **shared memory** doesn't scale well, the reason is that too many access to the memory create a bottleneck. An **MMU** is used to automatically assign the correct space to a specific process. 

**Cluster computing:**
Same as parallel computing but with a master coordinating the other pcs.

**Grid computing:**
A generalization of cluster and parallel computing. The idea is that in this case the nodes are **heterogeneous**. Grid also allow to use only part of a computer and not use all the resources for one specific purpose. An app is needed not an entire **OS**.
They use **virtual organization** (something like groups in Unix).

**Cloud computing:**
The basic idea is to offer virtualized resources based on SLA (rules). When you use something on a cloud computing infrastructure you don't know what you are actually using because there is a layer in between you and the infrastructure.
There are multiple examples: *IaaS*, *PaaS*, *IaaS*.
There are multiple layers in cloud computing, you can use parts of all the layers.

**Distributed pervasive systems:**
This is a concept pretty new. It applies to a network in which every aspect of our life is connected with the network. The system blends with the user's environment.
There are subcategories:
**Ubiquitous computing:** always present.
**Mobile computing:** the system physically moves.
**Sensor (and actuator) networks:** the nodes have a communication with the real world. They sense or deliver from/in the real world.

# Recap on threads:

Threads are basically virtual processors, used in software on top of physical processors.
Processor -> Thread -> Process.
Processes are managed by the kernel that allows to actually deliver the processes in the real processors (and/or cores). Processes can create multiple threads so that each thread can be delivered individually to the processor. Usually in modern system the scheduler always works with threads, a process is basically a single thread.

**Why use them:**
- Avoid needless blocking (when doing I/O etc.);
- Avoid process switching (Threads are much easier and less costly to switch).

**Actual advantages of threads:**
**TLP** measures the actual Thread-level parallelism. In practice the TLP is not really useful for speeding up things on the server side. They are usually useful to logically manage the program.
*Example:* an iterative server is much more complicated than a multithreaded one. It wastes much more time to handle a single request.
*Confusing example:* X window system (read more about it if needed)

On a server each application is usually reachable through a specific port and can be seen as a different server. Usually you have a super-server which assigns a port to each specific sub-server.

**Server clusters:**
In a server cluster multiple servers work to give a single service. With this logic you don't need to know the single machine you are talking with, the client only needs to ask for the service.
There are multiple ways of handling the requests, the main two are:
- **Transport layer switching:** The front end passes the TCP request to one server (using some kind of metric)
- **Context-aware distribution:** The front end passes the request based on the actual content of each single server.
Client side this part is usually transparent.

**Virtualization:**
The idea behind virtualization is to mimic the behavior of another system without modifying you real system. You have the illusion of using a different hw/sw than it actually is.

Virtualization makes code easier to port and also makes the code easier to maintain and upgrade. It also make it easier to manage the failure of specific components.

There are three types of virtualization:
- **Process VM**
- **Native VMM**
- **Hosted VMM**

In cloud computing virtualization is widely used. In IaaS the virtualization allows the user to use only the resources that he is allowed to use and is willing to pay for.

**Code migration:**
A first reason to migrate code is to make it so all the servers in a data center are heavenly loaded. Another reason is to make it so the computation are faster by moving the server phisically closer to the data. Another reason is to avoid needing to reinstall the same thing over and over.

**Models for migration:**
- *Client-server:* No code mobility;
- *Remote evaluation:* no code mobility, execution mobility; (Jupyter notebook)
- *Code-on-demand:* code mobility, no execution mobility;
- *Mobile agent:* code mobility and execution mobility.

**Migration of a virtual machine:**
Mobile agents were seen as the future, but nowadays the term more commonly used is **virtual machine migration**.
There are some alternatives to do this:
- stop and restart the VM;
- stop, move the memory and restart the VM;
- stop the VM, start a new VM and make the old pages available on-demand on the new VM.

Migration usually has an high cost in terms of time.
