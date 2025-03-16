# Intro to actual PenTesting

We will go into details on how to perform pentesting on **enterprise networks** as they are a lot more interesting to study and provide us with the possibility to actually asses vulnerability on the nets

*Note:* ofc you can also do vulnerability assesment on a private network, but it's not as interesting as all the vulnerabilities would be likely found in the single machines instead of in the network.

## GNS3

This tool is free and open source (it's an alternative to **Cisco packet tracer**) and it allows us to simulate a network. In this kind of tool there is the possibility to also integrate some non-free components by providing it with the proper files.

When we look at the tool we can easily create virtual networks using the default PCs, routers, switches etc. that are provided by the tool. We can also integrate other devices though images so that we can have **emulated** devices instead of only **simulated** ones.

## Segmentation

Usually we will refer as a net using the terms:

- **LAN:** Local Area Network
- **WAN:** Wide Area Network
- **DMZ:** Demilitarized Zone

**LAN** is the network that is inside the company while the **WAN** is the network that is outside the company.

*Note:* the term **WAN** might also refer to parts of the network that are outside the company but still inside the company's network. This happens often if the company is very wide or if it has multiple buildings that are geographically far from each other.

The **DMZ** is the part of the network that is still inside the infrastructure but **exposes ports and services to the word**. This means that this is the primary zone of attack for the infrastructure, at least as an entry point from the outside.

## Some devices

In this part we're going to see how all the theoretical stuff we've seen so far is actually implemented in the real world.

### Switch

This is a device that is used to connect multiple devices in a network. A switch is usually connected to one single **subnet**, this is because these devices are use for **infra-network** connections.

The switch is needed if we have two devices on the same subnet that want to communicate between each other. The switch is able to understand the MAC address of the devices and then send the packets to the right device.

Switches usually have physical ports that are connected to the devices and a management port that is used to configure the switch. The management port is usually connected to a router that is then connected to the internet.

The switch serves the **frames** to the devices, this is because the switch is a **layer 2** device. The switch is very efficient, since it's working on MAC addresses and cables, it's very fast and doesn't have to do any kind of broadcasting to know where to send the packets.

Usually it uses a table to know where to send the packets, this table is built by the switch itself by looking at the MAC addresses of the devices that are connected to it. The table is called CAM table. The table is automatically updated when a new device is connected to the switch. There is also a check on looping packets, that is to avoid the possibility of having a congested net if we use a broadcast.

*Note:* the table is updated when a packet is received by the switch, this is because the switch is able to understand the MAC address of the device that sent the packet. This might cause an issue in cases in which a device is added but doesn't send any packet. This is solved by using broadcast packets that are sent by the switch itself.

## Wireshark

Wireshark is another tool that is used to analyze the packets that are sent in a network. This tool is very useful to understand what is happening in the network and to understand if there are any kind of attacks happening. It's very powerful and allow to filter packets based on protocol, sender, receiver, etc. Using even complex regex or filters with a very specific syntax.

Wireshark can be used either live or offline. For the offline mode you need to have a file (usually a **.pcap** file) that contains the packets that you want to analyze.

Wireshark works on a single interface, the connection is usually between two interfaces so in this case you must be very careful and always take into account the fact that you are not analyzing "on the wire", you always analyze on one of the two interfaces of a connection

### Router

This is a device that is used to connect multiple networks. The router is a **layer 3** device, this means that it works on IP addresses. The router is used to connect many different networks and to route the packets between them.

In this idea we see the internet as a network of networks, the routers are used to connect them.

*Note:* we can see that in GNS3 by connecting at least 2 switched to manage the same number of networks to one single router so that it can handle those. (**OpenWrt** is a good example of a router's firmware that can be used in GNS3 for free, there are many different version, it's recommended to use the last one)

In the router you usually need to assign an IP address to both the network interfaces. Moreover you can also configure the firmware to integrate things like a firewall. When you install a firmware like OpenWrt or OpnSense then you **must** configure as by default they aren't usually going to work. For example by default LAN $\rigtarrow$ WAN is allowed but not viceversa.

### Firewall

Router and firewall are two different things. Even if that's true in reality there is usually a single device that can implement the functionality of both.

Actually a firewall can be seen just as a router that has a lot of rules to filter the packets or as an extension of the router that is used to filter the packets.

Writing good policies for a firewall is very hard and therefore sometimes they might be wrong. There are two reasons for that:

- The first is the fact that you usually know what is good and what is bad, but all the in between it's hard to address and consider correctly
- The second one is the fact that most of the time the net allows access to internet

You can write two types of lists: the first is **default deny** and the second is **default allow**. The first one is usually the best one as it's more secure, but it's also harder to write and maintain. The second one is easier to write and maintain but it's less secure because you aren't completely sure of what you're allowing.  
If you know what you're allowing you are very likely to be able to block most of the attack's surface. The problem is that most of the times it's also not feasible to use default deny if you want a user of the net to be able to access the internet.

Nowadays firewalls also have new security features and are therefore called **Next Generation Firewalls**. These devices are able to do many more things like:

- URL filtering
- application control
- creating VPNs
- support IPS and IDS
- etc.

Some of the most famous producers of firewalls (and routers) are:

- **Cisco**
- **Juniper**
- **Palo Alto**
- **Fortinet**
- **Check Point**
- etc.

#### Fortinet firewall

The first rule in the firewall is the so called **clean up rule**. This rule is used to block all the packets that are not allowed by the other rules. This is a very important rule as it's the one that is going to block all the packets that are not allowed by the other rules.

This firewall uses a web interface which is called **fortigate**
