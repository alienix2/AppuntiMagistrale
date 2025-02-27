# Pervasive systems and IOT

## Pervasive computing

The basic idea of **pervasive computing** is derived from what is standard nowadays, which is accessing computational power using the physical environment, without needing to access a device explicitly.

### Interaction with users

As said there is no single dedicated interface to allow the user to interact with the system. They are usually equipped with:

- **Sensors**: to collect data from the environment (and send it to the software)
- **Actuators**: to act on the environment (controlled by the software). In this case the user doesn't need to know what the actuators are. (*I.e:* he enters the room and the lights turn on, he gets the result without doing anything specific)

There are many kinds of pervasive systems like:

- **Ubiquitous computing**: the user is surrounded by computational power
- **Mobile systems**: the user is moving and the system is moving with him
- **Sensor networks**: the user is surrounded by sensors that collect data

#### Ubiquitous computing

The characteristics of ubiquitous computing are:

- **Distribution**: the system is distributed in the environment
- **Interactivity**: the system interacts with the user
- **Context-awareness**: the system is aware of the context in which it operates
- **Autonomy**: the system can operate without the user intervention
- **Intelligence**: the system can adapt to the user needs

#### Mobile computing

All of the above still apply in mobile computing, but in this case we are also considering a network which is constantly changing. We have **computer-line** devices but also less standard devices.

#### Sensor networks

This part is usually fundamental for the **pervasiveness** of the system. The sensors are usually small and cheap and therefore they have limited power. This means that there are many challenges to address when thinking of a sensor network.

The sensors aren't much smaller than normal computer. There are multiple ways in which data can be accessed in sensor networks like: sending messages between the nodes and moving code inside the nodes to access local data.

##### Sensors as distributed database

There are two possibilities in this case:

- Sensors send their data to a centralized database located on the operator's site
- each sensor can compute an answer to a query

### IoT architecture

The IoT architecture is made out of 3 layers:

- **Perception layer**: the sensors and actuators (This layer is made out of **perception nodes** and the **perception network**)
- **Network layer**: the network that connects the sensors and actuators
- **Application layer**: the software that processes the data

#### Perception layer protocols

There are many protocols that can be used in the perception layer like:

- **ZigBee**
- **BLE**
- **Z-wave**

#### Application layer protocols

There are also many protocols that can be used in the application layer like:

- **MQTT**
- **CoAP**
- **XMPP**
