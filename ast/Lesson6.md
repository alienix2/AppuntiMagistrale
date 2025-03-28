# Mocking

Mocking has a huge amount of detractors. It's a technique that is often misunderstood and misused.

The main problem that mocking aims to solve is the presence of dependencies in a single component of a system. It should be noted that it's very hard for a component to have no dependencies. Even very simple components are very likely to have dependencies on other components of the same project or external libraries.

When we write unit tests we must make sure that all the dependencies of the SUT are well tested and implemented correctly. In general we won't go into details of the actual implementations of the dependencies.

## Testing the state vs the interaction

When we do very simple testing we always try to test the state. This means that we look for returned values or the state of the SUT. In reality when need to test something that is more complex, we cannot think of always testing the state and we must therefore test **the interaction** of the SUT with the collaborator

*Example:* we consider a component that processes the elements returned by a database and then calls another method on the database (`update(args)`). We want to verify that the database's method is called only once with the right arguments or that it's never called under specific circumstances. (We assume that the function `update(args)` is correct)

Manually testing the interactions is very hard and the tests won't be very readable. Moreover you will also go against TDD

## Mockito

Mockito is a mocking framework that allows to create mocks and stubs following many good practices.

*Note:* check the examples for specific infos on how to do it.

### Stubbing with answers

*Note:* This part is optional (more on this on the book!!!).

This kind of stubbing is useful if we want a stubbed method to return something and that something will be calculated at runtime. This can be very useful if we have a method that you want to test and that method accepts a lambda exception as a parameter.

## Golden rule of Mocking

**Never** mock dependencies that you don't own $\Rightarrow$ **never mock 3^{rd} party libraries**.

If you need to use the library you should use another technique such as a wrapper or a facade.

## Test doublers and fakes

A test double is **anything that replaces a real implementation**. In our case these are just used as replacements for the real implementation that we will use in our tests. (A mock IS a test double)

A **fake** is another kind of test double. Fakes are effective implementations that are **much easier than the real ones**. *I.e:* the typical example of a fake is an in-memory database.  
The fakes must be write correctly and you must trust the fake implementation that you decide to use if you aren't writing it yourself.
