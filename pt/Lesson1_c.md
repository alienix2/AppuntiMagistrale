# Network theory

We're going to see in particular network attacks, this is why we should first understand how network works in general before being able to attack it.

An important thing to note is that in penetration testing you should have a very good knowledge on the whole ISO/OSI stack as an attack might exploit even the lower levels of it.

In reality the developers often work on layers. This is convenient but it might lead to some kind of vulnerability somewhere cause the software hasn't been properly tested as a whole.

*Note:* some low levels, like the physical layer, are usually not attacked. This is because it's very hard to attack them and also because they are usually very well protected.

We will look at the following layers into more detail:

- **Network layer**
- **Transport layer**
- **Application layer**

Which is where the most interesting things for us are.

## Network layers

### Physical layer

This is the layer where the actual bits are transmitted.

### Data link layer

This is the layer where the bits are grouped into frames. On this level there are some challenges that are assessed (like the possibility of a bit flip), but still in this layer the protocols are very simple and tied to their physical implementation.

The most interesting protocols in this layer are the ones that actually interact with the levels above like the **ARP** protocol that ties the IP to the MAC address.

### Network layer

This is the layer where the packets are routed. This is the layer where the IP protocol is. The IP is actually not a single protocol but a family of protocols. The most used one is the IPv4, but the IPv6 is also becoming more and more popular.

The IP is the base for network scanning, if we don't understand how it works than network scanning is going to make no sense.

### Transport layer

This is the layer where the data is actually sent. This is the layer where the TCP and UDP protocols are.

### Application layer

This is the layer where the actual data is sent. This is the layer where the HTTP, FTP, SMTP, etc. protocols are.

## Some basic concepts and names

**MAC:** Media Access Control, this is the address of the network card. This is a unique address that is assigned to the network card when it's produced. This is a 48 bit address. If you have multiple cards inside a device (a bluetooth one, a wifi one etc.) then each one should have a different MAC address. Every MAC is assigned to an IP, one of the most common ways to do that is using a DHCP that automatically assign it.

**IP:** Internet Protocol, this is the address of the device. This is a 32 bit address. The IP is divided into two parts, the network part and the host part. The network part is the part that is common to all the devices in the same network, the host part is the part that is unique to the device. The IP is assigned to the device when it connects to the network. It should be noted that 32 bits are not enough to represent all the machines on the net. This is why we have the NAT (Network Address Translation) that allows to have a single IP (**public IP**) for a network and then assign the devices inside the network a different IP (internally, **private IP**) that is then translated to the public IP when it goes out of the network. If you want a private IP address you must pay for it. (*Note:* more on them on the slides like IPv6, IP classes)

**URL:** Uniform Resource Locator, this is the address of a resource on the web. This is a human readable address that is then translated into an IP address by the DNS (Domain Name System) protocol.

**DNS:** Domain Name System, this is the protocol that translates the URL into an IP address.

### Address vs post

It's important to know the difference between the definition of address and port. Knowing only addresses is usually not enough as I don't really know the services that each IP address has attached (on different ports).

There are 65535 ports, the first 1024 are reserved for the most common services (well known ports). Some examples:

- ssh (22)
- http (80)
- https (443)
- ftp (21)
- etc.

*Note:* we should expect to have different ports than the standards one sometimes. These are just the standards one but the developers can choose any port they want. Given that some services actually function well on the default ports and therefore the developers usually keep them as the default ones (*I.e:* I know that a browser will look on port 80 or 443 so I cannot change that as it won't work otherwise).  
*Note:* a service might use multiple ports.
