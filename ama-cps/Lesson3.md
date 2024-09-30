# Managing time

The SoS are usually concerned abotu the passing of time. The problem is that as stated before the devices that compose a SoS are usually not synchronized automatically.

In SoS a global notion of time is required in order to synchronize the different systems.

## Basic definitions

**Time:** a continuous measurable physical quantity in which events occur in a sequence proceeding from the past to the present to the future.
**Timeline:** a *dense* line that indicates the progression of time from the past to the future. We can identify **Instants**and **Events** on the timeline.
**Cycle:** a temporal sequence of events which arrives at a final state from which the sequence of events can be restarted. *Note:*The main issue of cycles defined this way is that the duration is not defined.
**Period:** a cycle marked by a constant duration between the related states at the start and end of the cycle.

**Periodic system:** a system where temporal behavior is structured into a sequence of periods.
Control applications rely heavily on the systems being periodic.
*I.e:* I consider a system with a bus and some ECUs that need to communicate wit each-other using a central coordinator. Without sharing a clock anyone would have to communicate at random times, and noone would be able to understand when and why packets are colliding. We rely on the concept of time by considering a certain chunk of time and having each ECU communicate in a specific slot of that chunk (chunk=period in this case). This way all the collisions are avoided and it's well known who is communicating what and also in which period. There are some constraints, each slot should be sufficient for the message to be sent and received. Also usually each ECU sends an empty packet in his slot so that the other know that he is working properly even if he doesn't have anything to send.

## Time standards

The **physical** second is the same in all the commonly used time standards.
**UTC** is a standard defined by the rotation of the heart, which is, in fact, not constant. For this reason the SI decided to use the International Atomic Time (TAI) distributed by the GPS
**GPS** uses the TAI time which doesn't always align with the UTC.

**Clock:** a clock usually has an oscillator and a register. Whenever the oscillator completes a period an event (tick) is generated and the register is incremented.
**Reference clock:** a clock that is aligned with TAI and of granularity smaller that any duration of interest (for us).

**Coordinated clock:** a clock synchronized within stated limits to a reference clock that is spatially separated.
*Note:* the coordinated clock cannot be just created to be as close as possible to the reference clock because of costs. Usually we define an "interval of confidence" that we can consider acceptable in our system. *I.e:* in the previous example we define a grace period that allows the packets to be sent a little bit earlier or late.

## Coordination of clocks

We consider a few values which allow to identify of how much a clock is shifted from the perfect clock:
- precision $\pi$ (internal clock synchronization)
- accuracy $\alpha$ (external clock synchronization)
- drift (how many part of a unit of shit I have every one milliont of a second)
*Note:* drift can be hard to correct cause it can be so small that correcting it could be worse than better.

**Assumption made:**
- Every system has some kind of system drift. So the first assumption that we make is that a system will have a certain maximum value of drift.
- We do the same for accuracy and precision. *I.e:* the grace period discussed before is based on the supposed precision.

**Formal definitions:**
- **Drift:** drift of a physical clock is a quality measure describing the frequency ratio between the physical clock and the reference clock.
- **Precision:** maximum distance accepted between two clocks
- **Accuracy:** maximum distance accepted between the internal clock and a specific function
- **Offset:** distance of the perfect clock from the actual clock

**How to detect and adjust incorrect time:**

There are two main methods:
- the one used by GPS: this technology uses 20 (?) geostationary satellite. Each satellite sends data every second. The time necessary for the signal to reach the heart (**TOF:** time of flight) in a specific point is constant all the time(Cause the satellites rotate with the heart). Based of the TOF we know how much we should compensate. The satellite communicate with each-other to determine their reference clock (based on their atomic clock).
- the one used by PC: **NTP** (network time protocol). This is based on a hierarchical clock synchronization taking into account the clocks of all the devices connected. Each device has an atomic clock and is therefore able to help generate the reference clock.
**See the slides for the math part on how to calculate the offset!!!**

## Data and information

**Data:** a data is an artefact, a pattern, created for a specific purpose
**Information:** something that is able to represent a thing which is true in real life.
**Metadata:** information about data

Data can be meant to be received by a machine or by human. In both cases the data should be modelled so that the receiver can extract information from data.

**State:** the state of a given system is the totality of information from the past that can have influence on the future behavior of that system.
*Note:* the concept of state without the concept of time is meaningless, as we can note from the definition given above.

**State space:** the totality of possible values that the system variables can assume.

## Event based view and state based view

**Event based:**
The value of the variables are updated when an event happens.
The main problem of the **Event-based** view is that if the number of events is unbounded then number of possibilities to analyze is unbounded too.
*I.e:* I consider a car purchase. Someone purchases a car, the state of the car changes from "for sale" to "sold".

**State based:**
it is usually based on a periodic state-based view. This technique is called sampling.
We consider the value of relevant state variables at specific observation instants. The sampling interval must be chosen wisely and also in general it's a limit on the data generated by the view.

One is not better than the other, they have different use cases.
*Examples:*
- Axle counter used in the railway system. We must work with an event-based view cause we must know when the axle gets pressed.
- Semaphore for trains. A human can easily stop when he sees that the semaphore is red and start when he realizes that the semaphore becomes green, this way of thinking about it is clearly event based. An automatic system can do the same but it must work with a state-based system cause the camera analyzes the state of the semaphore as the time passes (and checks at small intervals of time).

## Time triggered systems vs Event triggered

A **time triggered system** is a system in which actions are triggered by the passing of time. Basically each component of the system is authorized to do something by the passing of time.
**Execution time:** time needed to execute a specific action on a system
**Worst case execution time:** the worst case data independent execution time required to execute an action on a given computer (WCET). *I.e:* time needed to access data in a fully loaded system.

*Note:* in an **event-triggered system** actions are usually triggered by some other event than the passing of time. A system can be both event-triggered and time triggered.

**Real time system:** a system in which a specific action (or task) is finished within a specific deadline. In order to create a real-time system you must evaluate the WCET and then set the deadline accordingly.

## Behaviour of a system

We consider a **function** as a mapping from a set of input values to a set of output values.
We consider **behaviour** the timed sequence of effects of input and output actions that can be observed at an interface of a system.
A system can be **deterministic** or **non-deterministic**.
A system is **deterministic** if the same input always produces the same output.
A system is **non-deterministic** if the same input can produce different outputs. (Usually this comes with the use of concurrency)

## Communication

**Message:** a data structure that is created to exchange information between two systems. They are supposed to be sent overtime.
There are different kinds of messages:
- **Datagram:** a message that is sent without any guarantee of delivery. *I.e:* UDP
- **PAR-Message:** a message that is sent with the guarantee of delivery. *I.e:* TCP
- **TT-Message:** a message that is sent with the guarantee of delivery and with a specific deadline and periodically. *I.e:* TDMA

The main difference as we can see are the guarantees that the message will be delivered and the time in which the message will be delivered.
Other characteristics of messages are:
- **message jitter:** the difference between the time the message is expected and the time the message is received. (In PAR is usually large, in TT is smaller)
- **temporal error detection:** in the PAR message this is done by the sender whereas in the TT message this is done by the receiver.

## Stigmergy

With this concept we go into the physical part of the cyber-physical systems. Until this moment we were always talking about the cyber part.

**Stigmergy** is a term which was first used in biology to describe the behavior of ants. The idea is that ants leave a trace of pheromones on the ground. The other ants can sense the pheromones and follow the path. The more ants follow the path the more pheromones are left on the ground. This way the ants can find the shortest path to the food.
In cyber physical systems we can give a description of stigmergy as follows:
**Stigmergy:** a mechanism of indirect coordination between agents or actions. The principle is that the trace left by an action stimulates the performance of a subsequent action.
*I.e:* in a smart city, the cars can communicate with each other by leaving a trace of information on the road. This way the other cars can sense the information and act accordingly. In particular, an ambulance can be seen or heard, pedestrian can look at traffic lights etc. Another typical application are the sensors of a car, that detect if it's going to hit the car in front of her.
