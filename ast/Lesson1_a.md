# Introduction to tests

An automated test is:

- a repeatable process
- verifies correct behavior of the entity under test
- specific to a context/scenario
- with a given input
- asserting a specific output

*Note:* sometimes we might need to drop some of these assumptions but in general they should all be guaranteed.  
*Note:* the output isn't always a direct return (in example a void method doesn't return anything)

It should be easy to understand what the code does by looking at the test. It should be noted that the documentation seems like it's doing the same but in fact the tests can be much better cause they must always be updated alongside the code. This means that using tests **as** documentation, this means that you are sure that the code is documented.

An important thing to note about automated tests is that they don't guarantee the absence of bugs on a pass but they **do** guarantee the presence of a bug on a fail.  

**Quote:** never trust a test that you've never seen fail.

**False positives** are the worst thing in automated tests.

It's very likely that if you have a part of your code that you havn't tested, a bug in your code will be in that part of the progrm. Moreover if you know that all the code is tested and the program is still bugged then you should write a test that reproduces the wrong behaviour so that you can identify the bug.

## Test Pyramid

There are many versions of the pyramid, we will focus on one of the most common approach and version of the pyramid.

### Unit tests

These are tests that are run on a single programming unit in **isolation**. Guaranteeing isolation can be easy on very simple programs but much harder in a complex structure.

A way of guaranteeing isolation is using **mocking** (that will be covered later during the course).

### Integration tests

These test multiple units togheter. Moreover these should be run only when the single units have been tested on unit tests.

### End-to-End tests

These tests basically test the whole application. This means to test the whole application **from the user perspective** so all the test should be run using the user interface. You don't actually have to test the internal behaviours (ofc they should already be tested with the other kinds above).

### SUT

A SUT means **System under test** (or something like **Subject under test**), basically it represents what we are testing.  
*I.e:* in a unit test the SUT is a single method of a class, in an integration test the SUT will be composed of at least two objects (but could be many more)

### Why a pyramid

In this case we have a pyramid like this

E2E tests  
Integration tests  
Unit tests

This basically tells us that we should have a lot of fast unit tests, some integration tests and a few of E2E tests. This is because the ones at the bottom are very fast and the one at the top are very slow.

*Note:* you are supposed to write few Integration and E2E tests mainly cause they are very slow to run, you shouldn't expect them to be fast, they just cannot be as fast as unit tests. Moreover they are also usually harder to write.

*Note:* in general if you don't know how to write the E2E tests using the GUI then you should just avoid writing them. (for the course you cannot skip them though lol).

### White-box vs Black-box tests

A white-box test is a test in which you know all the internal details of the class they are testing. Unit and integration tests are usually seen as white-box.  
On the other end the E2E tests are usually seen as black-box tests in the sense that they cannot use the internal knowledge of the class.

*Note:* integration tests are kind of in the middle, they should use a white-box behaviour without using too many information that would render the test useless.

### UI tests

These kind of tests are used for the user interface. They can be used to test a GUI or a CLI or a web app (tipically). They are pretty much needed for the E2E.

*Note:* UI tests and E2E tests are orthogonal in the sense that an E2E test usually include UI tests but the viceversa it's not always true. Even knowing that, it should also be noted that UI tests in general are hard to write and might take some more time than other tests (for example if we write a UI unit test).

### When to run tests and how

Tests should be run as often as possible (at least unit tests). We should have no problem running tests often and after every change we make.

Integration and E2E tests are usually run in a dedicated **continuous integration** server.

**Unit tests** should include all the possible situations a method could fall into. For example if I have an if option I should test all the possible paths. Also it should be noted that I cannot think of testing **all** the possible imputs, but I can try my best to still test all the paths with the fewer number of values possible.

*I.e:* if a method can fail (maybe in many different ways) I should test all the possibilities in which I want the method to throw an exception.

*Note:* usually each path should have one single test. This means that I can test multiple cases of a single path in a test.

#### Order in which to write unit tests

1. You write the **happy path**
2. You go on and write all the other paths one at a 09:44

**Integration tests** shouldn't follow the same logic though. This is because the single paths of all the components of the integration tests have already been tested. This means that we should only code the **interesting cases**. Unfortunately what is "interesting" depends heavily on the single application so each case must be analyzed singularly.

### Reaction to changes

Unit tests are very likely to fail if you change a single detail of the method they are testing. On the other hand the integration and E2E tests shouldn't usually be impacted so heavily.

We will use a tool for **mutation testing** that will verify that when changing a thing at least one test will be failing after.

### Concrete tests

The tests should always avoid having too many abstraction. Each test should be readable in isolation because without this property the tests aren't going to serve well as documentation.

### What to avoid testing

In general if something doesn't have logic you shouldn't test it. The classic example of this is **getters** and **setters**, also because many times those are auto-generated by the IDE.

*Note:* static type checking and tests are both necessary, they don't serve the same purpose.
