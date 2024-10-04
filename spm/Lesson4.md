## System design

**Goal:** Create a model of the system architecture that will be implemented. You also need to specify how they interact with each other.  
Usually in this part we follow some architectural patterns.
Some common architectures are: **pipeline**, **layered**, **client-server**, **data-centric**.

**Why we care about the architecture of the app in this course?**
Cause by knowing the architecture we can organize the work properly. If you don't decide how to breakdown the work for the project you won't be able to divide the work between the people who are working on the project.

## Implementation

This part involves the writing of the code. This is not a part that will be discussed in this course. Given that, this part is still important to consider cause you must consider what your developers are doing and how. There should be a way to understand how the work is going and if the work is going in the right direction.  
*I.e:* a metric that is usually taken into account for this part is the number of lines of code written in a day (or in the whole project). It must be noted that this metric is not sufficient at all, what the lines of code are able to accomplish is what really matters. We could say that this metric is good to understand if the work is proceeding but not to check if the work is going good.

## Verification and validation

**Verification:** is the process of checking if the software is being developed correctly.  
**Validation:** is the process of checking if the software we are building is the correct one.  
This part is known as V&V. The point is that the software should be good and well written, considering the requirements that we have defined. But we must also make sure that the requirements that are theorized are the correct one.

This part is usually done with testing.

## testing

There are different kind of testing that can be done:
- **unit tests:** these tests are done on the smallest part of the software.
- **integration tests:** integration between two components (or more).
- **system tests:** testing the whole system.
- **usability testing:** testing if the software is easy to use by the end user.

## Deployment

This part consists of actually installing the software in a real scenario. This part has some critical aspects such as the human factor and the hardware factor. *I.e:* are the people capable of using the system? Is all the hardware available and working.
There are many different approaches to deploy a software. Some of them are:
- **cut-over:** you just switch from the old system to the new one.
- **parallel approach:** you run the old and the new system at the same time for a period of time.
- **phased approach:** you deploy the software in phases.
- **piloting:** you deploy the software in a small part of the organization and then you deploy it in the whole organization when you have done proper testing.

Most of the times in big organizations there is a group of people that is dedicated to the deployment of the software.

## operation and maintenance

This part is needed to ensure that everything runs smoothly. Usually there is a team that is dedicated to this part. This team must work in contact with the customer.
There are many different kind of maintenance that can be done:
- **corrective maintenance:** fixing bugs that become apparent after the software is deployed.
- **preventive maintenance:** fixing bugs that could become apparent in the future.
- **adaptive maintenance:** changing the software to work with new hardware or software.
- **perfective maintenance:** adding new features to the software or improving the existing ones. 
