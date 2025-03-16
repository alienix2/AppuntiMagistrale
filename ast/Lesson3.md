# TDD

TDD is an approach that works. If you follow all the rules in the correct way there is no way that it can fail. Applying TDD in the correct way you are forced to follow a set of good practices. *Note:* you might be able to follow them even without using TDD, but it's good to follow a methodology that allows you to just follow them without any additional effort.

This approach is used for **unit tests**.

## Red-Green-Refactor

The TDD cycle is composed of three steps:

- **Red**: write a test that fails
- **Green**: write the minimum amount of code to make the test pass. (Make sure the rest of the tests are still passing)
- **Refactor**: clean up the code. (All tests should still pass)

*Note:* at very cycle the tests and the code should work on a single functionality.

The test that you write in the **red** phase **MUST** fail because it's trying to test a functionality that it's not yet implemented. If the test isn't failing then it must be a false positive or it's not testing the right thing.

*Note:* having a test failing at first and then having it pass instantly after the feature is implemented is a good way to **test the test itself**.

Since you will have to do many iterations and at the refactoring phase you should run **all your tests** then this means that this methodology forces you to focus on writing small tasks that you can test easily and also to write unit tests that are very fast.

### Things to do at each iteration

Some things to keep in mind while following TDD:

- Write quickly only the code to make the test succeed, you can be dirty and it doesn't have to be clean code.
- In the refactor phase you have a **safety net** because you have tests that will tell you if you broke something. *Note:* you **must** refactor the code if it's dirty
- If your code is clean already then you can skip the refactor phase
- In the refactoring you are not allowed to add new functionalities or to change the behavior.

*Note:* Also the tests should be clean and readable. A readable test isn't the same as a readable code.

### Why don't we write the code first?

Writing test after the code might be harder or even impossible. This means that we must go into the application and change it so that we can write tests for it. At that point we **should be afraid** of refactoring the code though cause we don't have the tests yet so we don't know if our refactoring will break something in the behaviour.

Moreover, writing tests after the code easily leads to **biased** tests. You are likely to write tests based on how the code already behaves, you don't even know which are the requirements most of the times.

If you write test in advance you are basically putting down **requirements** in advance. Tests can be seen as a **formal specification**, (even if they can't guarantee the absence of bugs)

TDD is a methodology that forces us to think about what the code should do before writing it. Moreover it also forces us to concentrate on what single task at a time, making it impossible to go over and writing a very big chunk of code in a single iteration.

### KISS (Keep It Simple Stupid)

This is a principle that is very important in TDD. You should always write the simplest code that can make the test pass. This is because the simpler the code the easier it is to test it. This requires to acquire the skill to decompose complex tasks into smaller and simpler ones.

## The 3 laws of TDD

Using TDD you write tests and production code at the same time. (Meaning you switch between test and production code continuously).

The 3 laws of TDD are:

1. You are not allowed to write any production code unless it is to make a failing unit test pass.
2. You are not allowed to write any more of a unit test than is sufficient to fail, and not compiling is failing.
3. You are not allowed to write any more production code than is sufficient to pass the one failing unit test.

### 1st law

This law is the most important one. It forces you to write tests first. This is because if you write the production code first you are likely to write tests that are biased towards the code you wrote.

There's not much more to say about it, it's pretty straightforward

### 2nd law

This law is about writing the simplest test that can make the test fail.

As soon as the unit test fails you should stop and write the production code that makes it pass. Knowing that the test is **failed if it doesn't compile** this means that if you are writing test for a class that doesn't exist then you should **instantly** go and write that class so that the test can compile.

### 3rd law

This law is about writing the simplest code that can make the test pass.

As soon as the test you wrote then you should go to the next phase, refactor and then move on to writing another failing test. This means that if I have a test failing for a missing class then you should just write that class to make the test pass, not a single line more (and most likely not a single line of implementation in that case).

*Note:* following these 3 laws and the TDD is a lot easier if you use a good IDE that gives you the possibility to switch between the many different phases seamlessly

Introducing a bug in this cycle is not something that is very bad. That is because you are just going to have to roll back a few lines of code and not much more.

## Transformation Priority Premise

This is a set of rules that tells you what to do when you are in the **green** phase and you have to refactor the code. Is based on the idea that the **transformations** in this phase should follow a very specific order and therefore also the tests should be written in a specific order.

The first list was created by **Robert C. Martin** and it's the following:

1. ({}–>null) no code at all->code that returns null
2. (null->constant)
3. (constant->scalar) replacing a constant with a variable or an argument
4. (statement->statements) adding more unconditional statements.
5. (unconditional->if) splitting the execution path
6. (statement->recursion)
7. (if->while)
8. (expression->function) replacing an expression with a function or algorithm

This list is not complete and should be taken as a guideline. The idea is the following:

- You should always start from the simplest transformation
- More complex transformations should be applied only after applying the simpler ones

If you don't follow this idea you might end up having a production code that is equivalent and working but it's not as clean and efficient in terms of performance.

### Avoiding the impasse

The **impasse** is a situation in which you are forced to rewrite a whole method in order to make a test pass. Following the transformation priority premise you should be able to avoid this very easily.

## 3 strategies for the green state

The techniques we are going to see were first theorized by Kent Beck in his book:

- **Fake it**: return a constant and then gradually replace constants with variables
- **Obvious implementation**: directly write all the actual implementation
- **Triangulation**: generalize the code once you have two or more examples

*Note:* it should be noted that the tests are not a **formal proof** to find a solution of an algorithm. In general algorithms require formal proofs. The tests are useful in situation in which you are not sure about a solution but you cannot find a formal proof for it. (Or it's not feasible to find one for each and every single part of your code).

*Note:* if you are 100% sure that specific thing work **you can write a passing test** just for documentation purposes. If you have any level of uncertainty you shouldn't go for a passing test as it's very easy to produce false positives this way. If you are doubtful just avoid writing a test that you think might pass alreasy.

*Note:* Integration and E2E tests are not part of TDD and shouldn't be written to fail first.

*Note:* TDD is fast if you are used to it. If you don't take the time to learn it in the right way then you won't be able to ever use it successfully.
