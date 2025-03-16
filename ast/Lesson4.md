# Code coverage

Code coverage measures how many lines of code are executed when the application is running.

If **the application is a test suite**, code coverage can be used to determine how much of the code is covered by the tests.

*Note:* this assumes that the tests are written correctly and therefore that you are sure that the parts that you run are actually tested and not just "executed" (*I.e:* a test without assertions)

The idea of keeping track of the test coverage is that the bugs usually **rely in the untested code** so by having a high test coverage you are less likely to encounter bugs.

## Code coverage in Java

In Java we will need a specialized tool in order to evaluate the test coverage. The best tools take into account the different branches in branch expression as well as all the possibility of the boolean ones.

### Jacoco and EclEmma

Jacoco is the mainstream Java tool for code coverage. In particular we will use **EclEmma** which is an eclipse integration of Jacoco.

EclEmma is a plugin that can be installed in Eclipse and that will show you the code coverage of your tests. You should run the tests through the EclEmma plugin in order to see the coverage.

Running the tests this way will be a little bit slower but the code executed will be basically the same.  
The different Java editors will be colored in green, yellow or red depending on the coverage.

- Green: Covered
- Yellow: Partial coverage (*I.e:* only some branches are covered)
- Red: No coverage

*Note:* the eclipse integration isn't able to exclude the test classes from the coverage. This means that if you run the tests with EclEmma you will see the coverage of the tests as well. This doesn't really make sense and might lead to lower percentages of coverage being shown. This won't be a problem when using Maven. Alternatively the run configuration can be modified to exclude the test classes.

*Note:* when you realize that some parts of your code are detected as not fully covered then you should be worried, in particular if you thought that you had tested the whole code.

**How much coverage is enough?** Actually you should aim to 100% of the **important code** which means any code that contains logic. If you apply TDD then you should have 100% of the code covered by tests. A 100% test coverage doesn't guarantee that the code is bug free but it's a necessary condition for it to be.

## Mutation testing

Mutation testing is a technique to evaluate the quality of the tests. The idea is to mutate slightly the SUT, so in every mutation the SUT is mutated and called a **mutant**.

If at least one of our tests fails then we are ok, otherwise we have a problem. The problem is that the test suite is not able to detect the mutation.

In Eclipse we will use **PIT** with **Pitclipse**. Pit is a mutation testing tool that will generate the mutants and Pitclipse is the eclipse integration.
