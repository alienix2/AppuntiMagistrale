# Metamodel for CPSoS

When designing a meta-model for CPSoS we have to take into consideration many aspects. Trying to create something that really fits my model I might not be able to create a meta-model that complies with UML.

## UML Profiles

A **profile** is a subset of UML that is used to extend the UML language. It is a set of stereotypes, tagged values, constraints, and other UML elements that can be applied to a UML model.

This is very useful to add constraints to the model that cannot be implied by using simple UML. *I.e:* I have a vehicle class and a tire class. I want to add a constraint to the tire that there should always be exactly 4 tires.

A **stereotype** is defined as extension of a UML base metaclass or as a specialization of an existing stereotype.

**constraints** can be used in a profile to add constraints to the model. They can also be applied to **stereotypes**. *Note:* not all the constraints can be written in OCL.

**Lesson goes to Papyrus:** check slides for more information.

## OCL

**OCL** is a language that is used to define constraints in UML models. It is a declarative language. The reason why OCL was created is that UML is a graphical language and it's not always easy to add constraints to the model. Before OCL most of the constraints were added only in natural language (or omitted at all).

*Note:* there are specific cases in which OCL constraints could be expressed through the use of standard UML, but it's usually better to use OCL for automatic validation.

OCL is one of the few alternatives that we have to add constraints to the model. It's not very easy to use but it's the most effective (probably).

With OCL is also possible to define queries on the model. This is very useful when we have to extract information from the model. This is also why it's useful to learn OCL, it can be applied not only to UML but to meta-models in general and also query languages.

### Creating statements

In order to create a statements we must start with a context. The context is the class that we are referring to. There are also some predefined contexts like `self` that refers to the current object.

*Note:* check the slides for an example on OCL used for modeling Meely/Moore machines.

*Note:* check slides for examples on AMADEOS and emergence.
