# Algorithmic techniques for estimation

There are two main kinds of algorithmic techniques, **function based metrics** and **size based metrics**.

## Function metrics

The **function based** approach makes it easy to estimate the functional complexity and it doesn't depend on a specific programming language. It's harder to link to productivity and they are harder to measure than size metrics

## Size metrics

The **size metrics** approach is based on the idea that the size of the project is a good indicator of the effort needed. This also means that someone can be evaluated on how much he worked based on how many **lines of code** he wrote. The main issues are the fact that writing a lot of code doesn't mean that the code is good and the fact that some languages make it so it's actually harder to think about the code than to write it, so a crucial line could require a lot of time to be written. There are some metric approaches that take into account the **semantics**. *I.e:* I consider a line a "semicolumn statement" so some lines will be counted as one and some line could even count as more than one.

## Function points

The function points are based on a combination of program characteristics derivable from the requirements. This technique is widely used.

The main steps are:

1. Define the **buondary** of the analysis
2. measure a set of characteristics related to the functional requirements of the system and use a formula to get the UFP (**unadjusted function points**)
3. measure a set of characteristics related to the **non-functional requirements** and compute the VAF (**valued adjustment factor**)
4. compute the **adjusted function points** (AFP) as the product of UFP and VAF (or with another function)

### UFP

The UFP is made of:

- **User inputs:** the number of different inputs that the user can give to the system
- **User outputs:** the number of different outputs that the system can give to the user and their complexity
- **User inquiries:** the number of different user inputs that generate a software response (word count, search result, software status ecc.)
- **Internal logical files:** the number of different files that are created and used by the system dynamically
- **External interface files:** the number of external files that connect with the software from an external system.

#### UFP program characteristics

The counting of UFPs is performed by looking at the requirements. The **analyst** looks for **DET**, **FTR** and **RET** (data element types, file type referenced, record element type). The tables are used to divide the numbers into the five characteristics. *Note:* training is required to understand how to use this technique properly.

#### UFP formula

$$UFP = \sum_{i=1}^{5} [k_i^E k_i^A k_i^C] \times [n_i^E n_i^A n_i^C]^T$$

Where:

- **UFP** is the unadjusted function points
- the value of the constants is provided by the method for each type i
- the value of n are the number of easy, average and complex elements of type i that we forecast

In this way the UFP provides an estimation of the functional complexity and size of the system.

### VAF

The VAF is a measure of the **non-functional requirements**. The VAF is composed of questions to which we need to answer and assign a value to each question in our project. *Note:* all the questions are about non-functional requirements like "the system requires data entry?" or "the system requires a local data backup?"

Then the VAF formula is computes as:

$$VAF = \frac{65 + \sum_{i=1}^{14} C_i}{100}$$

## After the FP

Once you have the function points you can use the value to evaluate the time needed to complete all of them in relation to how many people you are going to use. *Note:* on the Moodle page the prof. Provided an excel template.

Other than that you can covert the FP to a SLOC (source lines of code) and use another estimation method (*I.e:* COCOMO)

*Note:* the FP method has advantages and disadvantages. The main advantage is that it's language independent and it's based on the requirements. The main disadvantage is that it's hard to measure and it's hard to link to productivity and that means that someone with high knowledge is needed to make a good estimation using FP.
