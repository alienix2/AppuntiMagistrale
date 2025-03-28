# Banner Grabbing and enumeration

## Banner Grabbing

Banner grabbing is the process of connecting to a service and then reading the banner that the service sends back. This is useful to understand what kind of service is running on the port.

In order to perform banner grabbing we can use the `telnet` command or alternatively we can use the `nc` (netcat) command.

### Metasploitable2

Metasploitable2 is a vulnerable machine that is used to practice penetration testing. It's a virtual machine that is available for free and that can be easily attackable as it has many vulnerabilities.

### Metasploit

Metasploit on the other hand is a framework that is used to develop, test and execute exploit code. It's a very powerful tool that is used by many security professionals.

### Grabbing an OS banner

This procedure can be harder than what happens for other services as usually you're not going to get a direct information simply by contacting it.

What we can do is trying to find a **fingerprint** of an operating system (**active mode**). Basically we want to determine if the OS can be identified with the information that we can gather. This is usually done by looking at the **TCP/IP stack** of the OS.

The alternative is using what is called **passive mode**. One of the most common tools is **P0F**. In the passive approach we won't interact with the OS directly, we will just listen to network traffic involving that node. This works as different OSs may use different heuristics in order to establish and manage connections.

*I.e:* by default linux uses 64 as TTL while window defaults to 128.

## Enumeration

Enumeration is the process of identifying the services that are running on a target.

### Samba

Samba is a service well known for its vulnerabilities (*i.e:* **EternalBlue**). It's a service that is used to share files and printers between Windows and Linux systems.

The reason why this service is a good entry point is the fact that it interacts with other parts of the OS and therefore it can be used to gain access to the system.

Samba is a TCP service that runs on port 139 and 445 by default. With nmap we can check if those ports are used by netbios-ssn and microsoft-ds services.

There are many tools that can be used to enumerate Samba services. One of the most common is **enum4linux** that can do a full scan with one single command: `enum4linux -a <target>`.

### Default credentials

**Default credentials** can be seen as a kind of **weakness**. A weakness can be seen as a mistake in the way people reason. Many services and software provide very weak defaults, that **should** be changed before starting using the service but most of the times people don't do that.

The default credentials are usually defined by the manufacturer and are well known as they aren't seen as something that should be kept secret (and also shouldn't be kept in any production scenario).

A very common default credential attack is usually performed on very simple devices that people decide to install in their work environment without having care of the security implications. *I.e:* a webcam, a printer installed by a non-IT person.
