# Review of the test of previous Friday

## Polymorphism

There are 3 kinds of polymorphism:
- ad-hoc polymorphism
- subtype polymorphism
- parametric polymorphism
Modern programming languages provide all the 3 of them (Go only provides 2 of them)
Main advantages are: cores reusability, maintainability and flexibility.

**Ad-hoc polymorphism:**
When we define functions or operator with the same name that work on different types. This is usually achieved by **overloading**. 
**Subtype polymorphism:**
This refers to the ability of one type to be replaced by another type (they usually must share the same superclass)
**Parametric polymorphism:**
This allows a function or a data type to be parametric or generic on the types of its data. (*Example:* generics in Java or wildcards)

*Note:* There is another type of polymorphism that some authors define as polymorphism but some don't, it's called **duck typing**

## Static vs instance methods

**Static and instance methods:**
**Instance methods:** they are tied to a specific object (an instance of one) of a class.
**Static methods:** they are associated with the class itself and can be called without creating an object.

*Note:* in Go instance method are really a thing

## Abstract classes vs interfaces

**Abstract classes vs Interfaces:**
- **Abstract class:** it's a class that can have both abstract methods and concrete methods. It can be extended
- **Interfaces:** completely abstract type that contains only abstract methods (and sometimes default implementations). An interface is a contract that classes must adhere to. The point is to specify a behavior that can be shared across unrelated class that you want to be able to communicate with each-other. They must be implemented. A class can implement as many interfaces as it wants but can only extend one class.

*Note:* In Go we have no abstract classes, we have some kind of interfaces

## Balanced bynary search tree

**Balanced binary search tree:**
**Tree:** undirected graph in which two vertices are connected by exactly one path
**Rooted Tree:** a tree in which a special node is chose as **root** from which we can have a relationship of father-child between the nodes.
**Binary tree:** rooted tree in which every node has at most 2 children
**Binary search tree:** a binary tree in which all the values of the keys in the left subtree of a node are smaller than the node's value (greater for the right subtree).
**Balanced binary search tree:** a bst in which the difference of the heights of left and right subtree of each node is less or equal than a certain treshold (1 or 2 usually).

## Depth-first search and Breadth-first search

Algorithms used to traverse or search in a **graph**. (*Note:* a tree is a graph, but this Algorithm also works for other type of graphs)
For more details, look online. It's very important to note that this works on all the graphs

## Algorithm that given two sorted arrays returns a sorted array made from the two

The best way to do this is basically using the merge algorithm used in mergesort.

## Main differences between TCP and UDP

They are two most used protocols in the transport layer on the internet.
**TCP:** connection-oriented and reliable *Example:* SSH
**UDP:** connectionless, is not reliable (it can use some form of verification on the packets) *Example:* video-streaming. *Note:* UDP is also used in the cases in which you have limited resources.

## Three-way handshake

**SYN:** kind of packet used specifically for synchronization.

Client -SYN-> Server
Client <-SYN-ACK- Server (Server sends the response to the SYN of the client and his own SYN)
Client -ACK-> Server (Client sends the response to the SYN of the server)

*Note:* is this is not completed correctly there may be potential issues like a SYN-float attack.

## Main way to identify a computer online

**Domain name:** human-readable label
**IP address:** unique numerical label assigned to a device
**MAC address:** hardware identification number

## Race condition

A race condition is something that happens when two or more threads access to a shared resource and at least one of them is accessing in reading mode.
If they aren't synchronized there might be issues in the use of the resource.

Synchronization mechanisms:
**Mutexes**, **Semaphores**, **Barriers**, **Condition variables**, **Read/write locks**, **Atomic operations**

## Deadlock

The deadlock happens when two or more precesses never make process cause they are waiting for each-other to release resources.
The condition necessary are:
- **Mutual exclusion:**
- **Hold and wait:**
- **No preemption:**
- **Circular wait:**

To prevent deadlock we just need to avoid one of these conditions.

## System calls

A system call allows us to request a service that user-space programs cannot usually access. They are in the operating system's API.
*Note:* in Go system calls are present, but we will usually use something that wraps them cause they are really low level and can cause issues if they are used poorly.

# Transaction

A transaction is a sequence of one or more operations that must be treated a single operation. Either all the operations are done or none is.
**Acid properties:**
- **Atomicity:** a transaction must be treated as a single
- **Consistency:** in our database we usually have constraints. The transaction that start from a consistent state must reach a consistent state
- **Isolation:** transactions must not interfere with each-other. They are usually executed in isolation, if a transaction is being executed no other transaction is being executed at the same time if they rely on the same resources.
**Durability:** what is done must persist.

## Relational vs Non-relational databases

**Relational database:** we have data organized in tables. Each row is a record and the table are connected with each-other through the use of keys. They use a defined **schema** that is defined at design time.
**Non-relational database:** They do **NOT** use tables. They use many kind of files (document-based, graph-based etc.). They don't define a schema at design time. The query are usually done with languages like JSON.
*Note:* for more in depth look the slides

## Question about the creation of two queries
**Look at the slides for the solution of the queries :)**
