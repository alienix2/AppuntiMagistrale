# Model driven engineering (MDE)

The reputation of code generators isn't really good. The basic idea is that you can use a generator to create the skeleton of the classes but after that if you modify the classes, the diagram is not going to be updated so it's useless.

**This is only a partial view**. We are going to talk about different kind of generators, we will use customizable, domain specific, languages and tools.

**DSL:** A DSL (domain specific language) is a language that is designed for a specific domain. This means that the abstraction and notations are suitable only for the stakeholders of that concern.

## MDE application

One of the first application of MDE is **code generation**, that's also the main one.

There are two main types of code generation:

- **Dumb:** the code generator is only able to generate simple classes
- **Smart:** the code generator is able to generate something more complex, including UI to integrate with the generated classes

The smart code generators are usually used in the context of **DSL** (Domain Specific Language), and they have specific scenarios in which they are particularly useful.

## MDD, key elements

The key elements of MDD are:

- **Language:** the language used to describe the model
- **Execution engine:** the engine that allows to bridge the gap between the model and the final code
- **Target platform:** the platform on which the final program has to run on

## Workflow

The workflow we are thinking about is the following:

- the user provides a specification of the system using a DSL.
- based on that model we can generate complex artifacts, including other models

The thing is that this is an over-simplification. In reality there are many things to take into consideration. In general everything that you can automatize through the use of DSL is something that you can also implement manually.

## Acronyms

There are multiple acronyms that are used in this field:

- **MDE:** Model Driven Engineering
- **MDA:** Model Driven Architecture
- **MDD:** Model Driven Development
- **MBE:** Model Based Engineering

Actually all of them represent more or less the same concept but they emphasize on different aspects.

## What is a model

There are many definitions that try to describe what a model is. (See the slides for all the definitions)

The basic idea is that a model should be able to answer a given set of questions in the same way the system would allow answering the same questions. *Note:* we usually consider a purpose for which the model is useful, *I.e:* a globe is able to tell us the distance between two countries without having to cross them, it's not able to show us the animals living in each part of the world.

The essential attributes are:

- **Reference:** it's a model of something
- **Purpose:** it's useful for something
- **Cost-effective:** it's cheaper to use the model than the real thing

**Definition:**
![modeling_definition](../Screenshots/modeling_definition.png)

## Meta-models

A meta-model is a model of models. This definition isn't very specific but it's the most common one. The idea is that a meta-model is a model that describes the structure of other models, it defines what elements a class of models can have.

**Example:** UML is a meta-model that describes the structure of software models.

We can also have a **metaclass** that is a class that describes the objects that can be created starting from a specific meta-model, so an object of a specific model.

We say that a model **conforms** to a meta-model if it respects the constraints defined in the meta-model. We say that an object is **an instance of** a metaclass if it respects the constraints defined in the metaclass.

The meta-models are the basis of the MDE:

![MDE_schema](../Screenshots/MDE_schema.png)

The meta-models are usually created using other meta-models (**Meta-meta-models**).

In the MOF specification this is the last level of meta-models. This is because we can say that the meta-meta-model conform to itself. (It is formally demonstrated, but we just think about the intuitive way).

*Example:*
![matrix_model](../Screenshots/matrix_model.png)
We can see that the properties are some kind of classes so it's not needed to add another layer upper.

When we will have to transform a model into another model we will need to have the models A and B conforming to two meta-models which themselves conform to the **same** meta-model, otherwise the transformation is not possible usually.

## Interoperability

The term **interoperability** can have many definitions, IEEE defines it as:

> The ability of two or more systems or components to exchange information and to use the information that has been exchanged.

In **Model-driven engineering** interoperability is a key issue, as it is necessary to integrate models and tools from different sources. This is particularly important in the context of **multi-modelling** and **multi-paradigm** approaches, where different models and tools are used to describe different aspects of a system.

## Verification and validation

**Verification** and **validation** are two key activities in the development of software systems. **Verification** is the process of checking that a system meets its specification, while **validation** is the process of checking that the system meets the needs of its users.

One of the harder things to do in model-driven engineering is to assess **non-functional** requirements. There are various techniques that can be used to solve the issue, the most common one is to use proper testing techniques.

*Note:* this is also useful for performance and reliability analysis.

## MBSE purpose

**Model-based systems engineering** (MBSE) is a methodology that uses models to describe and analyze complex systems. The purpose of MBSE is to improve the quality of systems engineering by providing a common language and framework for describing and analyzing systems.
