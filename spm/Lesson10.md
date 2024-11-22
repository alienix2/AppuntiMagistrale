# Estimation techniques

There are 3 main ways to estimate the effort needed for a project:

- **Expert judgment**
- **PERT**
- **Algorithmic techniques**

## Expert judgment

This technique is probably the easiest to establish, this is because is based on personal assets. The assumption that must be made is that the project uses a WBS.

There are two ways to do an expert judgment:

- **Top-down:** the expert starts with the evaluation of the whole project and then breaks it down into smaller parts.
- **Bottom-up:** the expert starts with the evaluation of the smallest parts and then sums them up.

*Note:* bottom-up is usually the one which is preferred.

## PERT

The PERT approach is a probabilistic approach. This means that all the estimations are considered uncertain and therefore **duration ranges** and **probability** of falling in a given range are used.

Three estimates are assigned to each task:

- **Optimistic** (O): the best-case scenario (would likely occur only 1 time out of 20)
- **Most likely** (M): the most likely scenario (modal value of the distribution)
- **Pessimistic** (P): the worst-case scenario (would likely occur only 1 time out of 20)

**PERT formula**:
$$t_e = \frac{a + 4M + P}{6}$$

The PERT is no longer widely used in SPM

## Algorithmic techniques

The algorithmic techniques are based on the idea that we want to have a way to systematically determine the effort required for a task. The main issue is that we don't specifically know all the variables that are needed to determine that.

The **solution** to that problem is to look at already existing projects/datasets. Starting from that we find correlations between them and then evaluate the importance of each variable.

**Advantages:**

- **Replicable**
- **Objective** (unlike expert judgment)

**Limitations:**

- **Data availability** (the size of the data and the quality of the data might not be sufficient to produce a good evaluation)

### Main algorithmic techniques

- **COCOMO**:

  - **Size based** it estimates effort, duration and team size based on the size of the system.
- **Function points**:
  - are a measure of the functionality provided by a system. The idea is to evaluate the system based on the functionalities that are provided by the system.

*Note:* these two approaches can be used in conjunction (FP to get the system size and COCOMO to do the rest).
