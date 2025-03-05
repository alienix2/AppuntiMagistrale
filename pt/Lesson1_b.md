# Network attacks

We will see the basics of networking and the attacks that we can perform on the network, which are fundamental to understand the rest of the course.

## Endpoints

Endpoints are the devices that are connected to the network. Some examples are computers, printers, routers, switches, **smartphone**, **tablets**.

When you perform an attack nowadays you usually attack an endpoint. This is because you can actually exploit not only the software flaws but also the flaws in using it. Basically if the user uses the software wrong, you can attack it a lot more easily.

Another point in attacking an endpoint is the fact that the software on the endpoint **might be outdated**. This means that it might be running a specific version of a software that can be attacked with a specific known vulnerability (or with a vulnerability that you found and it's new).

*Note:* In reality many attack can start from a physical device, like a USB stick. This is because the user might plug it in and execute the software on it, which can be malicious. **We wont' cover that part** we will focus on attacks performed from remote

## Phases of a network attack

1. **Information collection**
2. **Network scanning**
3. **Access the network**
4. **Maintain access**
5. **Cover tracks** (cancelling the traces of the attack, like the logs)

*Note:* in real attacks a variation of these steps is actually used. In reality there are 32 steps that might be required but only some of them are actually used for every specific kind of attack.  
Interestingly if you look at the OWASP list of the most used vulnerabilities over the years you will realize that the most used ones are always the same.

*Example:* **Wannacry** was based on only 2 vulnerabilities on SMB (Server Message Block) and RDP (Remote Desktop Protocol).

A network attack is usually inserted in a **penetration test**.

### Phases of a penetration test

1. **Information gathering**
2. **Network scanning**
3. **Enumeration**
4. **Vulnerability assessment**
5. **Exploitation**
6. **Post-exploitation**
7. **Reporting**

The **report** is a document that gives a full list of the steps that have been done to exploit the vulnerability and also how to reproduce them. It's fundamental to se that the vulnerability is actually exploitable and not just theoretical.

If you don't find anything in the **vulnerability assessment** phase you can basically stop with your activity and declare that the system is actually secure (at least from your point of view and to the attacks you have performed).

There are many different kinds of **exploitation** that I can have, some might be a lot more harmful than others.

#### Information gathering

In this phase we should try to gather as much information as possible. Ofc some pieces of information might end up being superflous but in this phase we should gather all that we can find in case it might be useful later.

#### Network scanning

In this phase we try to understand the network topology and the services that are running on the network. This is fundamental to understand what we can attack and how we can attack it.

*Note:* In Italy this part is already illegal actually and even if it's easy to perform this activity you are actually breaking the low if you do this. It should be noted that there are protocol that **must** do a network scanning so you are allowed to do that in some kind of way. Also this isn't inherently malicious and/or related to a penetration testing activity.

#### Enumeration

In this face we try to understand the services that are running on the network and the users that are connected to the network. The difference from the previous phase is that in this one we actually taking information from the net that we already scanned.

*Note:* once again, we take some data that it might seem like we aren't allowed to, but many times common protocols already need that kind of data, we are just going to use it and see it in a human readable way.

#### Vulnerability assessment

This is the main phase of the penetration test. In this phase we try to understand if there are vulnerabilities in the services that we found in the previous phases.

For this part you can rely on **automatic tools** or **manual analysis**. Also it should be noted that some unexpected behaviour isn't necessarily a **vulnerability**.

The vulnerability is when we actually get access to information or services that we shouldn't be allowed to see. *I.e:* I'm able to access a database as a super-user, this must be defined as a vulnerability. I'm able to to make my session crash and I must relog, this might be a bug, but it's not a vulnerability if this doesn't lead to something more.

In this phase you can usually start from known vulnerabilities and then try to find some variations of them that might work in your specific case. There might be many **false positives** in this phase, so you should be careful and try to understand if the vulnerability is actually exploitable. The automatic tools might give you many possible false positives, but with the analysis done by hand you can sort them out and find the POC for the real vulnerabilities.

The **POC** (Proof of Concept) is not braking anything, it's harmless but it's showing that the vulnerability it's actually there.

#### Exploitation

In this phase you actually try to get something out of the vulnerability you assessed. A classic example is the possibility to access to reserved data or privileges. If you can go deeper into the infrastructure you usually should pick the **worst case scenario** for the exploitation.

Another thing that you can do in this part is called **pivoting**. This is when you perform the previous steps (some of them) again, using the new data you were able to access in this phase, gaining access to a lot more data (possibly).

#### Post-exploitation

In this phase you try to maintain the access to the system. This is because if you lose the access to the system you might not be able to exploit the vulnerability again.

It should be noted that the system you attacked is probably going to understand that it was being attacked and possibly also how so you might not be able to perform the same attack two times on the same system.

The administrator may also make you lose the access to the system if he's able to change some firewall policies to block you out

#### Reporting

The final report should have a structure that describes well your methodology. One of the most important part that should be included in the report is the **remediation plan** which is basically a list of things that should be done to fix each vulnerability.

Each vulnerability should also have a **severity** that indicates to the owner how to improve the system in practice. Sometimes a system might not fix a vulnerability entirely but some kind of fixes should still be performed. *I.e:* I have a machine running a very vulnerable OS, I can add firewall policies so that no one can access it from outside.

*Note:* a report that just have check marks on some test run is not a good report. You should also include a way to **replicate** the same steps that you did to try to exploit the vulnerabilities, even if you found no vulnerability.

*Note:* in general these points work in general, for specific use cases some other points might be needed or better to follow. Also some companies might have developed their own way to do penetration testing that has proven to be more effective for their use case.
