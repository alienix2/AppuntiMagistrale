# More on the PNs

The PNs are related to something actually existing, in particular:

- **Place:** components of a system, kind of components, state of a component or a resource etc.
- **Token:** component of a sytem, an event etc.
- **Amount of tokens:** state f a component, task waiting for a service etc.
- **Transition:** happening of an event, a task, a service etc.

## Modeling power

Those PNs are useful for representing some kind of dependencies like:

### Causal dependencies

This can represent the situations in which the execution of an action is possible only if some other action has been executed before.

This happens if the enabling degree of a transition grows after the firing of the others. Using this logic I can represent both **sequentialization** and **synchronization**.

The **conflict** situation happens between two or more transitions if both are enabled and the firing of a transition decreases to 0 enabling the degree of the other transition.  
In this case the firing of a transition disables all the others conflictual transitions.  
*Note:* the new marking may depend on the order in which transitions fire.

The **concurrency** situation happens between two or more transitions if both are enabled and the transitions can fire in any order without changing the enabling degree of other transitions.  
*Note:* in this case the marking doesn't depend on the firing order (but only on the initial marking).

*Note:* in general concurrency doesn't mean that also parallelism must be present.

The **confusion** happens when **both** concurrency and conflict exist at the same time, this means that either:

- in the same marking there are transitions that are concurrent **and** and conflictual
- The occurrence of a conflict **depends on the firing order** of concurrent transitions
