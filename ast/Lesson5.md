# Maven

Until this point we always used the IDE directly to handle not only the writing of the code but also the running of the code and the handling of dependencies.

## Why use an external program

In this course we want to have something more, something that also works with **continuous integration servers** and also something that allows us to automatically **compile**, **run tests** and **check for errors** **without the use of an IDE**.

The use of such tool is basically mandatory for a middle size project where there are many tests and more importantly if some of them require a lot of time to run. *Note:* if the tests require several minutes (or even hours) we can't think of running them through an IDE and watching them be executed on our computer.

Some of the dependencies that we will use (and some we already used) are:

- Junit4
- AssertJ
- Log4J

Those dependencies require many jars, one is not enough and moreover some of these dependencies require more than one jar on their own.

Another thing to note is that not only the dependencies are required be the main code, some of them are only necessary for the test code and therefore shouldn't be needed to run the main code.

When we release our code in the end we will have to ask the users to download all the dependencies that are needed by our code. If it's a library or a framework other developers will need to also download all the dependencies of our library, if the product is meant to be used by a final user we could even thing of just **pack the dependencies** in our jar but only those that are needed at runtime.

In any case handling the dependencies manually that needs a big effort and it's error prone.

## Using Maven

Maven is the **main stream standard build tool** for Java projects. It can handle **build automation** and **dependency management**.

*Note:* in other languages there are build tools that are integrated directly inside the language, that is not the case in Java and therefore we need to rely on some kind of external tool.

### Maven life-cycles

Maven has a very strict life-cycle. We should be very careful in following it as otherwise it will be very counter-intuitive and hard to use.

It has some hooks that allow for customization, that is everything you should use to customize the life-cycles in some kind of way, you should not **try to fight maven, you will lose**.

*Note:* the main alternative to Maven as of now it's **Gradle**. Gradle is much less strict, this means that you are much more free to make errors and moreover that you aren't going to be able to easily understand the Gradle project made by someone else.
*Note:* A big advantage of maven is also the fact that your package is automatically uploaded to the **maven central** without the need to maintain a server to track all the releases of your software.

Maven can be used to release some artifacts (mainly jars) but also to execute some collateral operations like **creating a complete release** and **deploying it on a remote site**.

### Maven convention

Maven approach is heavily based on conventions instead of configurations. What's the consequence of that? You don't need to tell maven how to compile and test your code, you can just follow Maven's conventions and everything will work (*sources:* "src/main/java", *tests:* "src/tests/java")

*Note:* if you don't follow the conventions you chose not to follow them but **you must specify maven how to use your code** at that point.

### Maven plugins

Many plugins are available for Maven. You can easily download them from Maven central using specific directives in the maven's configuration file.

In general in order to use Maven's plugins and to use it to handle dependencies you need to have an internet connection. It should also be noted that usually after the first time you download something it **will be cached** inside the `.m2` folder.

The jars also have a digital signature, this means that you can reassured that the jars you download from the Maven central will not be tampered with.

*Note:* if your `.m2` folder becomes too big then you might think about cleaning it every now and then so that you don't keep cached dependencies for projects that you are currently not working on.

### Installing Maven

Maven can be installed by downloading the binaries directly from the official website and then adding it to the PATH. The process is OS dependent.

Maven **is already included in the Eclipse IDE for Java developers**. If you don't plan on using Maven outside eclipse you can even think of avoiding the download of the binary.

### Using Maven from Eclipse

In order to start a project using Maven we can use the so called **archetypes**. They are useful to start very simple projects, some of them are officially distributed by the Maven team while others are created by the community (but still distributed on Maven central, typically).

*Note:* when you use an archetype to start a Maven project, that **is not going to be an Eclipse project**, still this kind of project can be imported inside Eclipse by using the appropriate wizard. When we do that we will have the `.classpath` and `.project` files added, creating effectively an **Eclipse Maven java project**.

The best way to create a Maven project to use in eclipse is actually creating directly with the wizard inside Eclipse, this way you will automatically have a Maven Java project.

### The pom.xml

**pom** stands for "Project Object Model". The language is **not imperative** (meaning no if then else or loops).

Maven is test oriented and as we saw is also based on conventions. Using m2e Eclipse plugin to create the project we automatically get the correct folder structure in order to follow those conventions.

Maven automatically runs the test inside the `src/test/java` as Junit tests and also the binaries of the test classes inside that folder won't be added inside the final jar of the output.

Maven can also pick which Java version to use for compilation and for running the code (after the jar is created). It's also possible to specify the encoding.

### Maven coordinates

Every maven artifact (dependency or plugin) is determined by coordinates (GAV):

- groupId
- artifactId
- version

These information **must always be specified**

#### GroupId

The convention for GroupId is the same as the java packages one. Basically it's the **reversed Internet domain name**. (*Note:* this convention was not so strict, for instance Junit uses `junit` and not `org.junit`).

Nowadays that convention is very strict, you are required to prove that you are the owner of the groupId that you want to use and moreover you are also required to provide a groupId.

If you don't own a company you can use github and your username *I.e:* `io.github.<your_user_name>`, you will be asked to prove that you are the owner of that account.

#### ArtifactId

Using something meaningful and using the `-` notation

#### Version

This represents the specific release of the artifact. It consists of alphanumeric literals and dots. You might have a temporary version by using the `-SNAPSHOT` suffix, every "work in progress" version should have this suffix.

*Note:* if you publish on Maven central using the `-SNAPSHOT` suffix your version will be published in a separate repository and will be removed when a normal version is released.

*Note:* the releasing of a real version can be handled with Maven itself using specific plugins.

### Maven dependencies

Dependencies are specified inside the `pom.xml` file. The structure of the dependencies starts from a `<dependencies>` tag and then inside that tag we have a list of `<dependency>` tags.

It's possible to specify the scope of the dependency, the default scope is `compile`. The other one that are we going to use in the course is the `test` scope. The scope defines were the code can be used and also if the dependency is a transitive one or not.

The `compile` dependencies become **transitive** for the project (meaning that another project that has this one as dependency will also need to have the compile ones as dependencies) while test ones are **not transitive**.

*Example:* when we use Junit we should specify it as a test dependency, this way the users of our library won't need to download Junit in order to use our library.

### Eclipse m2e

The Eclipse m2e plugin is a bridge between Maven's dependency management and the Eclipse compiler and classpath. One of the very useful things it does is automatically setting the scope of Maven dependencies in the Eclipse project's classpath. By default the sources and Javadoc are also downloaded.

The compilation should be performed manually. The m2e does a good job in keeping also the compiler settings in sync with the Maven settings.

*Note:* the Eclipse compiler is not the same as the Maven compiler, the Eclipse compiler is not the standard one and most importantly **it's incremental** while the java standard one is not.

### Version of dependencies

The specific version of a dependency can be specified in the `pom.xml` file. By changing the version in the `pom.xml` the new version will be downloaded (if not already present in cache).

*Note:* in Eclipse we have specific tabs that allow to see and manage the `pom.xml` file in a more graphical way. It's not necessarily faster and/or better as the XML file is very simple and easy to understand.

Maven automatically downloads and handles the transitive dependencies. *I.e:* if we use Junit we don't need to specify that we also need `hamcrest`, it will be automatically downloaded.-

### Properties in the pom.xml

It's possible to define properties in the `pom.xml` file. This is useful to avoid repeating the same version in multiple places. The properties are defined inside the `<properties>` tag.

It's also possible to change the properties from the command line by using the `-D` flag. This is useful to change the version of a dependency without changing the `pom.xml` file.

*Example:* `-DdbDriver=MariaDB` will change the property `dbDriver` to `MariaDB`.

### Maven project

A folder with just a `pom.xml` file is a Maven project. Using maven as a build tool requires to have a more specific file structure (of course).

Using maven as a build tools requires maven to be able to perform a series of tasks that an IDE does seamlessly but that have some complexity in them. *I.e:* the tests always refer the **already compiled** main code, so the order of compiling is relevant.

### Maven life-cycle

This concept is probably the most important one to understand to use Maven.

*Note:* the concept of life-cycle in Maven is a typical oral question

**Life-cycle**: an ordered list of phases with associated **goals** that in this case are provided by the Maven plug-ins

This means that the plug-ins can attach tasks in the phases that they want to work into. Some goals are bound by default to specific phases but they can also usually be attached to phases by hand.

Maven has 3 main life-cycles:

- **clean**: removes all the files of the previous builds
- **default**: generates all the artifacts
- **site**: generates the documentation of the project

#### Phases of the default life-cycle

There are many phases in the default life-cycle. They can all be seen in the official documentation: <https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html>

The phases aren't automatically executed, they are only executed if they are bound to a goal. The goals are the tasks that are executed in the phases.

#### Running Maven from the command line

You can run Maven from the command line using the `mvn` command. You can specify the phase that you want to run. The command is `mvn <phase>`.

*Note:* you might want to run multiple phases at once, you can do that by specifying the phases in the order you want to run them.

*Note:* the command `mvn clean install` is the most common one that you can find online. This command works but **is wrong** general as those two phases probably do way too many things.

When you request to execute a phase, first all the previous phases in the life-cycle are executed, in the order in which they appear in the life-cycle.

When a phase is executed **all the goals that are defined by the plug-ins activated in the pom that are attached to that phase are executed**.

#### Default plug-ins

There are some plug-ins that are automatically activated by Maven. They are automatically attached to the phases of the life-cycle.

*Example:* the plugin attached to the `clean` phase by default is the `maven-clean-plugin`. This plugin cleans the **target** folder so **it's usually useless to run it if you didn't previously build the project** already and therefore need to clean that folder.

An important maven default plugin is the `maven-compiler-plugin`. This plugin is attached to the `compile` phase and it's used to compile the code.  
By running `mvn compile` we are executing the goal `maven-compiler-plugin:compile`. **BUT** we are also executing the goal resources of **maven-resources-plugin** before that.

### Maven build

The build of a Maven project is a very complex process. The build is composed of many phases and each phase is composed of many goals.

When a single goal **fails** then the build is **interrupted** and the whole build is considered **failed**.

### Maven packaging

Every Maven project can have only one packaging. Every Maven project also inherits from what is called a **super pom**, the super pom is related to the installation of Maven and is the parent of all the poms by default.

#### Parent pom (inheritance)

A pom can have only one single parent pom. All the configuration of the parent pom are automatically inherited and if not specified also the **groupId** and **version** will be inherited.

The structure of the directory that allows to use the concept of a parent pom is very important.

If the parent pom lists all the child poms then it's called an **aggregator** pom. Normally when we talk about a parent pom we don't mean an aggregator pom, but a pom that doesn't have the `<modules>` tag.

Most of the time the aggregator pom is also used as the main and only parent pom, but there can be **multiple aggregator poms** even if one pom can only have one single parent pom. When you separate the two responsibilities then the aggregator pom has to mention also the parent pom alongside all the child poms

##### Dependency management

The parent pom can also manage the dependencies of the child poms. This is useful to avoid repeating the same dependencies in multiple poms. By default all the children will have the same dependencies as the parent but this can be overridden, adding specific dependencies only to specific modules.

##### BOM

The BOM (Bill of Materials) is a special kind of pom that is used to manage the dependencies of the child poms. The POM can be imported in from another Maven project.

*Note:* the version number is kept consistent across all the modules.

#### Maven "Reactor"

The Maven reactor is the way that Maven uses to handle multi-module projects. It's able to automatically understand link between modules and to build them in the correct order.

### Enabling and configuring a Maven plugin

What must be specified:

- GAV of the plugin
- The goal to execute
- If necessary, the phase to which attach the plugin
- The configuration of the plugin

*Note:* you should always also consider that every packaging type has some plugins enabled by default. Therefore you should look at the **effective POM** to spot them. A plugin's goal might be associated with a phase but not enabled by default.

In the section `<executions>` there can be multiple `<execution>` tags. In the outer section `<configuration>` you should include all the configuration that is common to all the executions. Inside the `<execution>` tag you should include the configuration that is specific to that execution.

*Note:* the POM is very verbose but besides that it can easily be checked statically. In the Eclipse editor you can see the errors in the POM file if they are present.

In the effective POM when we **merge** a configuration with another one the last one wins. This means that if we have a configuration in the parent pom and another one in the child pom the child pom's configuration will be used.

### Maven profiles

Maven profiles are defined by using a `<profiles><profile>` tag. Each command has an ID and can be enabled manually by using the `-P<id>` from the command line.

In the profile we can also specify the JDK version to use. It's also possible to specify a max and min JDK version.

*Example:* we can configure a jacoco profile. This might be useful as we don't want to always run Jacoco because it slows down the execution of the tests quite a bit. Same thing can be said for the mutation testing plugin.

*Note:* the order is not relevant in an XML file. There are some conventions to make it more readable but in general the profiles could be found anywhere in the XML.

*Note:* the profiles should be used to extend the build in some circumstances, not to change it completely. For instance a build that only passes with a specific profile but fails with no profiles, is not a good build.

## Maven wrapper

The maven wrapper it's just a script that checks if the specific version of Maven necessary for the project is installed. If it's not installed it downloads it and then runs the command that was passed to it.

To create a Maven wrapper you need to have an installation of Maven. You can then use the command `mvn wrapper:wrapper` to create the wrapper and then use `./mvnw` to build it.
