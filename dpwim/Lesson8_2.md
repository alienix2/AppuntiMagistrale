# Types of distributed systems

## High performance distributed computing

**Basic idea:** creating a super computer using off-the-shelf components or existing systems.

### Cluster computing

Good for parallel programming, the hardware is **omogeneous**

### Grid computing

Resources from different organizations are put together. There is no assumptions on the omonogeneity of the hardware (**heterogeneous**).

## Distributed information systems

**Basic idea:** sharing information between different systems.

The main issue could be the **interoperability** and the management of **transactions** (a series of commands that must be executed as one).

## Pervasive systems

These systems are designed in order to integrate with our environment. There is a large use of sensors and actuators. The system should be dynamic cause nodes come and go really fast.

## General misconseptions

- **The network is reliable and/or secure and/or homogeneous:** this is clearly false on the internet
- **Latency is zero, and the bandwith is infinite:** this is physically impossible
- **There is a single administrator:** this is not true when you start to integrate different systems that already operating. You are now the one who administrate all of them
- **There is shared knowledge:** this is not true, if a component doesn't explicitly share information the other nodes won't know it.
