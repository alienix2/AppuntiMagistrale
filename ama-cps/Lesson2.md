# System of systems

Starting with chapter 1 of the book but much more detailed.

**Computing evolution:**
- 60-70s computer fitted in one room
- 80-90s main frames where one user could connect from his pc to use it's power
- 00s ubiquitous computing. Computers everywhere, almost everyone already has a PC (usually more than one). Embedded processors for specific purposes are more and more developed (*I.e:* fire sensor, it is composed of a material that melts when there is too much heat)
- 10s Cyber Physical systems. systems which are composed both by hardware (cyber) and software. *I.e:* a modern car

**Cyber-physical systems:**
- **Cyber:** digital, this is the computation and communication part
- **Physical:** real, governed by the laws of physics
The human can be involved but it could also not be involved.

**Monolithic vs today:**
The mainframes were thought as monolithic systems, that means that they weren't supposed to be upgradable and changed in general. Nowadays this mentality has completely shifted.
Mainframes had everything inside them, they were not modular and they were not easy to upgrade at all both hardware and software wise.
There still exist monolithic parts of systems:
*I.e:* a **Monolithic kernel** is still present in Linux. Linux is still considerable (and considered) modular, things can be added to the monolithic kernel.

**SoSs (System of Systems):**
- the scope of the system is usually uncertain
- there doesn't need to be an acceptance test as the final phase
- faults aren't considered something exceptional and should always be handled properly

*Examples:*
- Helicopter: it's cyber-physical, it has a predetermined scope, the acceptance test must be done and faults are acceptable events (in theory at least).
- Railways: it's cyber-physical in the modern world, the scope is determined (there are multiple services but there is one big single goal); the acceptance test isn't really done in a classic way, you need to test directly on the field; the faults should be handled everyday.
- Vehicles stuck in traffic: each vehicle has to go from point A to point B. If you end up in a traffic jam vehicles must interact with each-other. Those vehicles are sometimes treated as SoSs even if they don't have (much) cyber interaction.

A SoSs usually stems from existing systems and new systems that take advantage from that integration. Basically the legacy systems become coordinated by creating a new system of system because a new systems needs them to cooperate with each-other. *I.e:* Alexa make a SoSs from all your home appliances.

Making a system of systems work somehow is usually easy, the hard part is making the system of systems robust, secure etc.
*I.e:* if Alexa breaks it can leave your light on or your windows open.

SoSs are strictly connected with IoT. What are the *main problems* that we have in IoT? Security, interoperability, cannot prove ROI, cost, hardware integration and maintenance.

**Application domains of cyber-physical systems:**

There are multiple domains in which SoSs are used. If we consider **automotive** for instance, we can think about specific implementations.
A car Nowadays has a defined scope. The design phase is not terminated with an acceptance test though because modern cars undergo system updates (like smartphones). Faults cannot be considered exceptional events, sometimes they can happen and they must be handled correctly.
Even if we consider autonomous driving, fault happen. We can think about robo-taxy in America, they have a few malfunctions but we are usually talking about the fact that it is too good at following the rules. Another accident that happened to a robo-taxy recently was that a pedestrian ended up in the wheels of a robo-taxy and the taxy kept on driving for many meters before realizing that something was wrong.
If we consider assisted driving these kind of accidents are less prone to happen.

**Multi-level hierarchy:**
SoSs usually have a multi-level hierarchy, or we could say a recursive structure.
A system can be divided into different systems (**macro-level**) and each single one can be divided into multiple subsytems (**micro-level**).
This recursion ends when the internals of a subsystem is of no further interest. Depending on the specific case it might be necessary to go into more or less detail.
*I.e:* I consider the railroad system. I might need to go into specific details of a single train station if I'm trying to build or improve a train station, I might need to go in-depth with the software details if I'm developing the code. In the first part I shouldn't care about the code at all.

**Monolithic vs System of systems:**
- Scope of the system: fixed vs Unknown
- Clock synchronization: Internal vs external (GPS)
- Structure: hierarchical vs Networked (it's conceptually hierarchical still)
- Requirements: fixed vs changing
- Evolution: version control vs uncoordinated (everyone can evolve differently)
- Testing: test phases vs continuous
- Implementation: technology is given and known vs unknown (this can of course cause problems sometimes)
- Faults: exceptional vs normal (faults, **NOT FAILURES**)
- Control: central vs autonomous (ofc there can be some sort of control but each system has some freedom of movement)
- Emergence: insignificant vs important (There will be a future lesson about that, the point is that a system could contribute in a system of systems without knowing)
- System development: process model vs ??? (everyone can develop on it's own, you must believe everyone is doing fine)

# Points of view

There are multiple viewpoints that we can have on SoSs and we will analyze all of them during the course.

**Fundamentals:**
- **Domain:** a domain comprises the set of entity and relationship between them. We add to the domain all the entities and relationship that we need to model a selected view of the real world.
- **System:** a system is an entity that is capable of modifying the environment and is usually sensitive to the passing of time.
- **Environment:** environment represents where we operate (*I.e:* a car's environment is the streets).
- **Boundaries:** A system must have defined boundaries, sometimes they are easy to understand, sometimes it can be harder to define them (*I.e:* a car should drive in in his own lane but the boundaries are hard to define cause the car must also be able to identify what happens in the other lanes and also more. If a pedestrian starts running from it's sidewalk inside your lane, you must predict this from before he enters your lane). Sometimes boundaries are not stable. (*I.e:* a car that goes slowly needs to know less information than one driving fast). 
- **System architecture:** blueprint of the design of the system. It defines the overall structure (it can go more in depth or less in depth depending on what we need).
- **autonomous systems** and **cyber-physical systems:** discussed before (and will be discussed more after).

**System of systems:** a SoS is an integration of a finite number of constituent system which are independent and operable, and which are networked together for a period of time to achieve a certain higher goal - "Jamshidi".
*Note:* here we say that the number of systems is a finite number. This way we give a limit to the number of systems involved.

**Types of system of systems:**
- **Directed SoS:** SoS with a central managed purpose and central ownership of all CSs. *I.e:* a car, a satellite
- **Acknowledged SoS:** Indipendent owners of the CSs, but they cooperate with each-other with strict rules. The purpose is aligned between all the owners. *I.e:* the aviation system
- **Collaborative SoS:** voluntary interactions of independent CSs to achieve a single goal. *I.e:* bitcoin miners, ATM networks
- **Virtual SoS:** no central purpose and central alignment. *I.e:* the internet **This is the single real example we can think of easily**

**Emergence:**
**This isn't related with emergency**
When we think of SoS we may think that it is only a sum of system but that's not the case. In fact emergence is used to represent the fact that the many systems interact with each other to create something on a higher level.
**Emergence:** a phenomenon of a whole at the macro-level is emergent and if and only if it is of a new kind with respect to the non-relational phenomena of any of its proper parts at the micro level.
*I.e:* the ATMs are connected, a user has a better service cause he can withdraw from all the ATMs but each ATM also works on his own.
The emergent phenomena can be positive or negative.
