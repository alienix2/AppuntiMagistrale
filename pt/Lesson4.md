# Network scanning

In this part we plan on using the tools we have learned to scan the network and find out what devices are connected to it. We will also try to find out what services are running on these devices.

## Honeypots

A honeypot is a computer system that is set up to act as a decoy to lure cyber attackers and to detect, deflect or study attempts to gain unauthorized access to information systems. The system is designed to be attacked and compromised so that the attacker's methods can be studied and that information can be used to increase network security.

It's also a way to make the attacker waste time and resources on a system that is not important, allowing to actually gain time to protect the real server. If there's a real threat that the system might be vulnerable then a very simple way to protect is to just put the system as a whole offline.

## TCP protocol

In TCP the **header** part decides how the protocol works.

### TCP flags

There are many flags that can be used and those actually change the behaviour of the connection. Some of them may even change it very widely.

The most relevant flags to us are:

- **SYN**: This flag is used to initiate a connection. It's the first thing that is sent when a connection is being established.
- **ACK**: This flag is used to acknowledge that a connection is being established. It's the second thing that is sent when a connection is being established.
- **FIN**: This flag is used to close a connection. It's the first thing that is sent when a connection is being closed.
- **RST**: This flag is used to reset a connection. It's the second thing that is sent when a connection is being closed.
- **PSH**: This flag is used to push data to the application. It's used to tell the other side that the data should be delivered to the application as soon as possible.
- **URG**: This flag is used to tell the other side that the data is urgent. It's used to tell the other side that the data should be delivered to the application as soon as possible.

### 3-way handshake

The 3-way handshake is the process of establishing a connection in TCP. It's done by sending a **SYN** packet, receiving a **SYN-ACK** packet and then sending an **ACK** packet.

This part is very easy to spot even by looking at the packets. The first packet will have the **SYN** flag set, the second packet will have the **SYN** and **ACK** flags set and the third packet will have the **ACK** flag set. Wireshark can automatically detect this and show.

A thing that you can do using nmap is to do the so called **SYN scan** which consists of sending a **SYN** packet to the target and then waiting for a **SYN-ACK** packet. If the target responds with a **SYN-ACK** packet then the port is open, if it responds with a **RST** packet then the port is closed. Usually even if you receive a **SYN-ACK** you then proceed to close the connection as you don't want to called system to record your connection. This procedure is silent but could be noticed by some tools running on the net (like wireshark itself) and pass as very suspicious.

*Note:* in this procedure we are also tampering with the TCP protocol so we are actually moving deep into illegal territory.

## UDP scan

Scanning the UDP protocol is usually harder to do than scanning the TCP protocol. This is because the UDP protocol is connectionless and there's no clear way to know if a connection is starting a UDP connection and moreover also to know if a port is open.

We can exploit the ICMP protocol to understand if a port is open or not. The problem is that the server might be configured in order to avoid sending this kind of ICMP packets to connections that are not allowed. This is a very common practice in order to avoid scanning and therefore if the port is usually defined as "closed **or filtered**" meaning that it might actually be opened.
