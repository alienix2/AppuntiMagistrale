# Autogenerated (I was absent at this lesson :( )

## Stigmergy (I) - Slide 79
- **Stigmergy**: Indirect coordination mechanism where traces left in the environment stimulate future actions.
- CSs exchange information through:
  1. **Conventional communication channels**
  2. **Stigmergic channels** (indirect coordination)

## Stigmergy (II) - Slide 80
- Originated in biology to describe ants leaving pheromones on trails to communicate.
- Successful trails have higher pheromone concentration, leading to faster movement.
- **Environmental dynamics** (e.g., pheromone evaporation) ensure unused trails disappear.

## List the stigmergic channels - Slide 81
- Channels for stigmergic communication:
  - Physical modifications in the environment.

## A typical application - Slide 82
- **Applications**: Autonomous systems, smart grids, multi-agent systems.

## Interfaces - Slide 83
- **Interfaces**: Interaction points between systems and their environment.
- **Channels**: Physical or logical links that transport information.

## Interactions over Channels - Slide 84
- **Interaction**: Exchange of information at interfaces.
- **Channel model**: Describes channel effects such as bit-error rate (BER) and bandwidth.

## RUIs - Slide 85
- **Relied Upon Interface (RUI)**: Where services are offered to other CSs.
  - **RUMI**: Relied Upon Message Interface.
  - **RUPI**: Relied Upon Physical Interface.
  - **RUS**: Relied Upon Service (with SLA).

## Other Interfaces - Slide 86
- **TSI (Time-Synchronization Interface)**: Establishes global time for time-aware SoSs.
- **D-Interface**: Diagnostic interface exposing system internals for monitoring.

## Dynamicity and Evolution - Slide 88
- **Dynamicity**: Short-term reaction to environmental changes.
- **Evolution**: Long-term changes or optimizations.

## SoS Evolution - Slide 90
- **Managed evolution**: Guided changes to keep SoS relevant.
- **Unmanaged evolution**: Occurs naturally due to changes in constituent systems (CS).

## Reconfigurability - Slide 92
- **Reconfigurability**: Adaptation to internal failures or service quality improvements.
  - Example: Graceful degradation in telecom networks.

## SoS Authority - Slide 93
- **Authority**: One party can demand changes in another system's configuration.
  - **Collaborative SoS Authority**: Manages RUI changes across CSs.

---

# Chapter 7: Dependability and Security

## Introduction - Slide 98
- Dependability involves the system’s ability to deliver a trustworthy service.
- **Security**: Ensures availability, confidentiality, and integrity of the system.

## Dependability and Security: Added Value or Commodity? - Slide 100
- Cyber-Physical Systems (CPS) are used in critical services often without human intervention.
- Dependability and security are essential for such systems.

## Infamous examples - Slide 102
- **Ariane 5 (1996)**: Incorrect component from Ariane 4 caused overflow and failure.
- **Mars Climate Orbiter (1998)**: Metric vs imperial unit conversion error led to mission failure.
- **Knight Capital (2012)**: Misconfigured software caused $440M loss in stock trading.
- **Patriot missile system (1991)**: Clock drift caused failure to intercept missile, killing 28 soldiers.

## Dependability - Slide 111
- **Dependability attributes**:
  - **Availability**: Readiness for correct service.
  - **Reliability**: Continuity of correct service.
  - **Safety**: Absence of catastrophic consequences.
  - **Confidentiality**: Protection against unauthorized information disclosure.
  - **Integrity**: Protection against improper system state alterations.
  - **Maintainability**: Ability to undergo repairs and modifications.

## The Means to Attain Dependability - Slide 118
- **Fault prevention**: Avoidance of faults.
- **Fault tolerance**: Ensuring the system operates despite faults.
- **Fault removal**: Reduction of the number and severity of faults.
- **Fault forecasting**: Estimation of current and future faults and their consequences.

## Verification and Validation - Slide 120
- **Validation**: Ensuring the product meets the needs of the user (Are we building the right system?).
- **Verification**: Ensuring the product is built correctly (Are we building the system right?).

## Security (I) - Slide 122
- **Security**: Composition of confidentiality, integrity, and availability (CIA triad).
- **Threat**: A potential adverse impact on the system through unauthorized access or actions.

## OWASP IoT Attack Surface Areas (2018) - Slide 125
- Top IoT security risks:
  1. Weak/hardcoded passwords.
  2. Insecure network services.
  3. Insecure ecosystem interfaces.
  4. Lack of secure update mechanisms.
  5. Use of insecure or outdated components.
  6. Insufficient privacy protection.
  7. Insecure data transfer and storage.
  8. Lack of device management.
  9. Insecure default settings.
  10. Lack of physical hardening.

## Discussion - Open Question - Slide 126
- For each example, discuss the main dependability and security requirements.
