# Junit

In this part we will go into the details of Junit and how to use it for testing.

## Phases of testing

### Setup

The first thing to do is to setup the SUT. In particular we must do what is called a **test fixture**. The test fixture is made of all the things that must be in place in order to test the SUT (so the SUT itself must be present but it's not the only thing needed).

A well done test fixture should ensure that the results are reproducible.

*Note:* in the first examples that we will see the test fixture will include only the SUT, but later on we will see what a more complex test fixture looks like. *I.e:* in a unit test the fixture will include the mocks, in an integration testing the fixture will include many real classes.

### Exercise

In this part we will actually run the SUT. This is the part where we will call the method that we want to test.

### Verify

In this part we go on and verify that the outcome of the tests matches what we were expecting. Usually for this we use **assertions**

### Teardown

In this part we clean up the test fixture. This is important because we want to leave the system in the same state as we found it.

This is very important for specific kind of tests, like tests on real files or database. This phase is necessary cause otherwise the test might not be deterministic and rely on the order in which they run or they might not work the second time we run them.

## Details of Junit

Junit is the standard framework used in Java for automated testing. We'll use Junit 4.13.2. We won't cover Junit 5 into detail but in the book there are infos also on how to use this new version.

*Note:* Junit isn't directly included in Java, so we need to add it as a dependency. The good thing is that Eclipse comes with Junit so we won't need to do anything if we plan on using the standard Eclipse Junit suite.

### Convention

Usually when we write a Java class, we will write a test class for it. The test class will have the same name of the class that we are testing, but with the suffix `Test`. *I.e:* Foo -> TestFoo

Once the class is created a method of testing should be created for each path of the original method of the class.

The name of the method doesn't have to follow a specific rule regarding Junit cause it only looks for the annotation `@Test`. There are convention that we should follow for readability and that will be seen later in the course.

### Methods in Junit

In Junit all the methods are public. There are some special annotations:

- `@Test`: this is the annotation that tells Junit that this method is a test method. This is the only annotation that is mandatory.
- `@Before`: this annotation tells Junit that this method should be run before each test method. This is useful for setting up the test fixture.
- `@After`: this annotation tells Junit that this method should be run after each test method. This is useful for cleaning up the test fixture.
- `@BeforeClass`: this annotation tells Junit that this method should be run before all the test methods. This is useful for setting up the test fixture.

So the **lifecycle** goes as follows: `@BeforeClass` -> `@Before` -> `@Test` -> `@After` -> ... -> `@AfterClass`. As it's usual for every framework and tool, you should **never mess with the lifecycle** if you don't like it avoid using that tool.

### Assertions

The assertions are Static methods defined in the class `org.junit.Assert`. The most common are:

- `assertEquals`: this method checks that two objects are equals. It's important to note that this method uses the `equals` method of the object, so if you are testing a custom object you should override the `equals` method.
- `assertTrue`: this method checks that the condition is true.
- `assertFalse`: this method checks that the condition is false.
- `assertNull`: this method checks that the object is null.
- many more...

We should always use these assertions instead of diving into using if/else checks cause the framework will handle this for us if we use the assertions.

If an assertion **fails**, the test will stop and the test will be marked as failed. If an **exception** is thrown the test will terminate with an error. Otherwise it will **succeed**.

*Note:* this behavior represents an **all or nothing** behaviour which means that either all the test succeed or fail cause if only one fails we will have a red or blue bar (fail or error).

### @Test

Each test should verify a single scenario. It's important to note that a single scenario isn't a single assertion. If verifying a single scenario needs **multiple** assertions that it means that you should include all of them inside a single test.

Even if that it's true a test **will fail** if one of the assertions fails. This might not be the best if we want to verify subsequent assertions all at the same time but unfortunately Junit4 doesn't allow the possibility to do that (Junit5 does).

### Order of execution

The order of execution **is NOT guaranteed** so this means that all the tests should be completely independent. You shouldn't rely on side effects from another test and you should never take into account the order that you know they are being executed at a specific time cause this might change at the next run and is very likely to change on another computer.

*Note:* ofc you can rely on the order of execution if you are using the correct annotation as stated above.
