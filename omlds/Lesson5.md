# Stochastic activity networks (SAN)

The four graphic primitives of a SAN are:

- **Place**: A place contains tokens and is used to represent the state of the modeled system
- **Activities**: They represent the actions of the modeled system. The activity is fired at completion
- **Input gate**: the input gate is used to specify the **enabling condition** of the activity and **changing the state of the network** when an activity ends
- **Output gate** is used for changing the state of the network when an activity ends

## Places

The places are depicted as circles. The number of marking in a place represents the number of tokens stored in that space and the marking of the SAN represent the set of all the marking of places.

A place **with its marking** is part of the state of the modeled system.

As usual the tokens are anonymous and their meaning is arbitrary.

## Activities

### Istantaneous activity

The activities are **instantaneous** and they have a **fixed priority** of 1.

### Timed activity

Duration or time of an activity: random variable defined
through a distribution function
Distribution of the time of activity: general, it can use any distribution (as long as it is supported by the tool)

Parameters of the time distribution of an activity: mathematical expressions depending on the marking

They represent actions that have a duration that impacts on the measure of interest of the modeled system

They have fixed priority 0

### Cases of an activity

A **case** represents the probabilistic choice between more alternatives. They are represented as two (or more) little circles placed on the right part of the activity.

Each case has a probability and moreover that probability is also **marking-dependent**, meaning that the probability distribution might change based on the markings of the network when the activity completes.

Activities without circles are like a single case with probability 1.

## Reactivation function

The reactivation function are a mechanism used to define the conditions depending on the marking which may allow an activity to be **reactivated** when any activity completes.

This means applying the **restart mechanism**: abort the activity discarding the current value of the timer and a new value of the timer of the activity (the time distribution is the same, even if the parameters can be changed)

## Input gates

These are represented by a triangle pointing to the left.

The enabling predicate is a boolean expression that controls if the connected activity is enabled

The input function defines how the markings change when the activity completes. The completion of the activity doesn't depend on the selected case

## Output gates

These are represented by a triangle pointing to the right.

They connect cases (or activities if cases are not present) to the places.

The output function defines how the markings change when the activity completes. When the output gate is connected to a case, the gate function is executed only if the case is selected when the activity completes.

## Completion rules

An activity can complete in a marking if:

- it's enabled
- there are no other activities with greater priority

*Note:* if more enabled instantaneous activities are in a marking, the choice is non-deterministic and therefore we are talking of a **not well-specified SAN**

An instantaneous activity completes after zero time since its activation. There can be a policy of competition or race that decides what happens when more timed activity are enabled. A timed activity can complete only if it's enabled for the whole time defined by the timer, otherwise it aborts.

Once an activity completes some steps are executed:

1. Choice of the distribution of the cases
2. Choice of one of the cases
3. Execution of the functions of the input gates
4. Decrease tokens in all the input places of the activity
5. Execution of all the output gates connected to the selected cases
6. Increase tokens in all the output places connected to the selected cases

*Note:* With the rules above we might end up with something that it's not deterministic, in particular if we look at step 3 and 4

The above numbers can be executed in any order but with some constraints on the fact that the marking generated **must not depend on**:

- the order in which the input gates are selected (in step 3) if tehre is more than one input gate connected to one activity
- the order in which the output gates are selected (in step 5) if there is more than one output gate connected to one case
- the order in which steps 3 and 4 are executed
- the order in which steps 5 and 6 are executed
