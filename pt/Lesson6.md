# Vulnerability assessment

This is the crucial point of the whole penetration testing process. The definition of what is a **vulnerability assessment** is different depending on the stakeholder that gives it.

Some definition were given by **OWASP**, **SANS** and **MITRE**.

One of the fundamental things that should always be included in a vulnerability assessment should be the **POC** (Proof of concept). This is a way to demonstrate that the vulnerability is real and that it can be exploited.

An **Exploit** is a piece of code that is used to take advantage of a vulnerability, a **vulnerability** is a weakness in a system that allows to perform operations that aren't normally permitted to the user.

Vulnerabilities are usually found in two ways:

- **Vulnerability scanners**: tools that are used to scan for vulnerabilities
- **Manual testing**: you find them by looking at a database of vulnerabilities and then you try to exploit them. Alternatively you can also use your own knowledge without looking at already known vulnerabilities.

The alternative is to find a **0-day** vulnerability. This is a vulnerability that is not known yet and you're the first to find it.

## Vulnerability scanners

These kind of tools are just tools that have many built-in exploits and try to run it on a target. Some might have heuristics that can slightly adapt the exploits to the specific case.

Some tools can be specific for a certain kind of vulnerability, others can be more general. *I.e:* **OWASP ZAP** can be used to find web vulnerabilities.

*Example:* In class we looked at **OpenVAS**

*Note:* the automatic scanners and all the tools in general are very cool but most of the times what you need to find are all **corner cases** and therefore they won't be easy to find.
