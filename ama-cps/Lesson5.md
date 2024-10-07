# Chapter 2
This chapter is still bit abstract, starting from the next one the work will be more practical.

## Interfaces
An interface in a system of systems are point in which a specific component of the system interacts with another component or with the environment.

One of the most important things in SoSs is to identify the interfaces and then to specify them and standardize them.

**Consituent system processing:**  
- **Itom received:** these are received by the cyber space or by sensors observing the physical state in **entourage** of CS. *I.e:* if I consider a server room one of the only itom is the temperature of the environment, I just need to identify if the temperature at which the servers are running is correct.
- **Itom produced:** these are produced by the CS and are sent to the environment or to the cyber space.

*Real world example:* I take into account an airplane cockpit. Some of the itoms received are: messages from the sensors to the autopilot and the cockpit, messages from a station to the plane. Some of the itoms produced are: messages for the station about the current position.

**Environmental model:**  
As the name states this is a model that is used to represent the environment in relationship with the system. In this model are represented the interrelationship between variables.

**Overlapping:**  
In the real world it's normal to have the entourages of different CSs overlapping. This allows us to consider stigmergy.

*To wrap up:*
- each cyber-physical cs is in a physical enviroment and has a physical entourage
- overlapping entourages allow for stigmergic channels and so we have an exchange of itoms

**Objective:** conceptualize time-sensitive interaction in CPSoS so that we can introduce interface layers and produce an effective design model.

## Interface layers

Dividing interfaces into layers allow us to discuss the properties of each interface and to define them in the specifications of the interface. The layers which are usually considered are:
- **Cyber-physical Interface layer:** level where messages interact with things and energy, in this layer there is an interaction between concrete technology and sensors/actuators.
- **Informational Interface layer:** level of the information Itoms. There is a first abstraction given from the previous layer that allow this level to ignore the interactions with the cyber part.
- **Service Interface layer:** level of the services. This level is necessary to create a SoA (**Service oriented architecture**) and is an abstraction over the individual information channel, basically it just serves an interface where information from the previous level is put togheter.

## Cyber-physical Interface layer
In this layer Information is represented by data items.  
The two main communication channels are:
- **RUMI:** this is the channel that allows the communication between the cyber and the physical part of the systems.
- **RUPI:** those are the channels that allow the communication between the cyber part of the systems. This is fundamental for stigmergy

*Note:* also a channel called **RUHI** could be considered for the communication between humans.

In this layer there is the exchange of the first Itoms. Also the information contained from the single Itom is refined and allows to produce information to be used in the higher level interface. 

## Informational Interface layer
*Example:* speed limit sign interpreted by an autonomous car. The car reads the sign, listens to other type of sensors and decides which is the best way to go to the right speed. In this interface time is a crucial factor.  
There are some things to do in this level:
- removal of details: the information is refined and the details are removed
- context-independent information flows
- Itoms are explicitly specified and refined.

*Example:* if a car has to perform an emergency break. At this level we have the car communicating with other cars to tell them that they should start to slow down too. (*Note:* the information that are needed for the single car are analyzed in the lower level as discussed above)

By using indirect channels multiple system of systems can create an **Environmental constituent system** that realizes the common environment of interacting CSs.

## Service interface layer
In this part I only care about what my SoSs can do in term of services. This layer is specifically used for SoA.  
The idea behind SoA is to start from the services themselves. Usually we consider each service as individual (or loosely coupled with others) and also every service should be quite small. There are two main components in SoA, **Rest** and **Soap**. On top of those there is usually an orchestrator which decides the order in which to call the single services, otherwise the services could be instructed to cooperate without the use of an orchestrator.  
Usually in SoA there are two actors: **service consumers** and **service providers**, without any of these two the service has no reason to exist.

**Interface Service Specification:**  
it's a set of quality metrics that allows to determine the quality of provided service. Service providers offer their capabilities under a **SLA** (Service level agreement).

## RUIs
A RUI is a Relied upon Interface. Is basically something that other components of the system depend on.
**RUI Connecting:** when we talk about RUIs we need to consider the RUI connecting strategy. The idea behind this is to search for available connections and then drop them if they are no longer needed.

**Roles of the RUI:**
- system boundary
- complexity firewall
- information transfer
- **Emergence**
- dinamicity
- evolution

*Note:* we can imagine how the different levels of the interfaces work in an RUI, for instance:  
**Cyber-physical level:**
at this level the different components of RUI interact with each-other as well as usually connecting to certain kind of sensors, like satellites for setting their clock.
*Note:* check images in the slide for more in depth

## Managing evolution
There are two models of evolution that can appen in a SoSs:
- **Managed evolution:** in this type of evolution you evolve a component in a way that doesn't change how the system works or if it does you know it from before starting the evolution
- **Unmanaged evolution:** this is the opposite. This usually happens cause someone else other than you decide to update something that your system relies on.

It can also be divided into two types of evolution:
- **local evolution:** this doesn't affect RUI, optimized CS 
- **global evolution:** this does change the RUI usually.

# Emergence
This part could be hard to follow cause it mixes information technology with some kind of philosophy.

The concept of Emergence is born from the quote "The Whole is greater than the Sum of its Parts", attributed to Aristotele (even if he probably didn't say it)

The most expensive part in developing a system is the engineering effort cost.

**Cognitive complexity:** this define how hard it is for someone that already works in the field to understand a given scenario for a given purpose.  
This is directly related to a mental model that can establish causal links between input, state and output observable on the system.

**Emergent phenomenon:** A phenomenon is defined as emergent if it is new with respect to the non-relational phenomena of any of its proper parts at the micro level.  
*Note:* an emergent phenomenon could be positive or negative.

One of the main points of SoSs is to obtain an emergent behavior. We want to make the different systems cooperate to obtain something that is emergent and cannot be obtained by using the single systems individually. This means that we don't actually know if an emergent behavior will actually rise from our SoSs, but we can try to define how to make it happen by using a correct way of modeling.

## Multi-level hierarchy
In a multilevel hierarchy each level has its unique set of laws. Emergence is always associated with levels of a multi-level hierarchy. Depending on the specific purpose I have I can identify when to stop going down in my hierarchy and select a level in which I want to work on. Let's start with an example of a multi-level hierarchy  
*Example:* We consider a Smart-Grid in which a blackout happens.  
To represent my system I consider a neighborhood, the energy provider, and an energy distribution. During the blackout we can think about the neighborhood asking for a quantity of energy that cannot be provided by the energy provider and therefore the blackout happens. To create a hierarchy I can start by dividing the neighborhood into every single house that it is made of. Every house has a different amount of energy it's asking.

**Holon:** a holon is a two-faced charachter that can is seen differently as a sum of entity at the micro-level and as a single entity at the macro-level.

**Holarchy:** a holarchy is a multi-level holon. This means that at each leyer there are holon that are creating another holon.
In a holarchy there can only be vertical interaction, called interaction-relation.  
The hierarchy is also fundamental in order to establish rules and have one point that can guide the others that are underneath. *I.e:* we can think about an orchestra, the director help the musician coordinate, but he doesn't need to know how to play each instrument and also doesn't specifically tell the musicians how to play.
