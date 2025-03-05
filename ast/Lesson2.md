# More un Junit testing

*Note:* github repo with examples from the book: <https://github.com/LorenzoBettini/tdd-buildautomation-ci-book-examples>

## Testing of private methods

Private methods are usually not tested as they should stay internal to a class. In fact you **should test the private methods using the public ones that use it**.

*Note:* a private method that it's not used by any public one is useless as no one can use it.

Moreover if the private method is too complex to be tested by the public ones, it's a sign that the class is doing too much (probably violating the **single responsibility principle**). The best idea is to refactor the class making it more testable but most importantly also improving it's design and making it more readable.

A very simple example of why a class has a private method is usually that it actually contains some part of the code that was duplicated in multiple public methods. This means that the method can indeed be tested from all the other public methods implementing that logic and using the private one. Also usually if you do this kind of refactoring it means that you already tested the lines of code that you are going to have in the private method and the tests will pass without any kind of modification.

*Note* this kind of refactoring is called **extract method** and is a well known kind of refactoring that is deterministic and **not based on AI**. In Eclipse there is some intelligent refactoring options that allow you to select multiple lines to automatically refactor, creating a new method and also replacing those same lines in all the occurrences in the code.

*Note:* for the exams it's **strictly forbidden to use reflection** to test private methods. This is because it's a bad practice and a code that it's not legacy should never need it.

## A little digression on JUnit5

JUnit5 has been created with modularity in mind. It has 3 main parts:

- **JUnit Platform**: it's the core of the framework and it's responsible for launching the tests and providing the APIs to write them. It's also responsible for the test discovery and execution.
- **JUnit Jupiter**: it's the new programming model for writing tests. It's the part that provides the annotations and the assertions. It's also responsible for the extension model. (basically it's the implementation of the above)
- **Junit Vintage**: it's a bridge that allows to run JUnit 3 and JUnit 4 tests on the JUnit 5 platform. This is useful because it allows to migrate to JUnit 5 without having to rewrite all the tests.

### Some simple differences

- **@Test** annotation is now **@Test** from **org.junit.jupiter.api.Test**.
- The tests can now be **package private** (default visibility) and they will still be run. Actually it's recommended to have the tests classes as package private even if in tests the visibility it's not so important.
- **@BeforeClass** and **@AfterClass** are now **@BeforeAll** and **@AfterAll**.
- **@Before** and **@After** are now **@BeforeEach** and **@AfterEach**.
- In assertions the message is now the last parameter and not the first one. Moreover you can now use **lambdas** to provide the message only when the assertion fails.
- There is now the possibility to also run all the assertions inside a test method even if one of them fails using **assertAll**. This is useful to see all the failures at once and not just the first one.
- Test methods can be annotated with a **@DisplayName** annotation to provide a more human readable name for the test. This means that you can also give names that include spaces or special characters.
- You can now use nested classes to group tests that are related to each other.

## Assertions

In JUnit4 the assertions are static methods in the **Assert** class. These kind of assertions are fine for simple tests but they are not very readable and they don't provide a lot of information when they fail.

To improve this we can use external libraries. In particular some of the most common ones are **Hamcrest** and **AssertJ**. Harmcrest is already part of JUnit4 but still it's syntax is not very readable. AssertJ is a library that provides a fluent API to write assertions in a more readable way.

**AssertJ** can be used by simply downloading the jar and importing it in the classpath. It should be noted that **this is not the best way to use it in general**, during the course we will see how to use it with maven.  
AssertJ uses a fluent API to write assertions. This means that you can chain multiple methods to create a more readable assertion, moreover it follows a syntax that is very similar to natural language and is therefore immediately easier to read.

AssertJ also try to do a good job in it's failure messages, not all the assertions return the same message, they have been designed to be as informative as possible. *I.e:* if I use `assertThat(1).isLessThan(0)` the message will be `expected:<1> to be less than:<0>` automatically.

For more complex assertions there is really no comparison and AssertJ is always easier to write and also to read and understand after.

*Note:* given that there are many assertions this also means that you might find many different ways to test the same kind of behaviour. Even if that is true there is usually one which is better than the others and should be preferred. Usually you should prefer the most readable one. SonarQube will check this
