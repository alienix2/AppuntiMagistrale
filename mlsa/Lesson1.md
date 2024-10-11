# What's program analysis

An example of program analysis is ChatGPT interpreting a code you send it. It can try to follow the value of a variable and also understand what's the program doing as a whole.

Machine learning is a way to train a machine so that it can do one job in an automatic way. (we have a machine, let's try to automatize it through machine learning).
Machine learning has trivial uses but is also used in critical use cases like public transport.

**Good software:**

- Correct
- Usable (*Example:* a user friendly social networks)
- Efficient (*Example:* a social networks that doesn't drain your battery fast)
- Reliable
- Secure
- Adaptable
- Accurate
- Robust
- Maintainable
- Portable
- Reusable
- Readable
- Testable
- Understandable
Creating software that matches all these characteristics is really demanding.
Today the majority of the time needed to write code is actually spent for testing, debugging etc. As a result in the software industry there is an increasing focus on using tools to write better software.

**Software and program analysis** refers to the process of examining and evaluating the software artifacts. The main goal is to improve things such as reliability, efficiency and readability.

There are two main approaches:

- **Static** analysis

- **Dynamic** analysis

**Static** analysis involves examining the software without running the code. It uses syntax checking, data flow analysis and more techniques. It uses tools like linters and reverse engineering tools.

**Dynamic** analysis involves analysing the code during the execution. Focuses on runtime properties like memory. The main tools are debuggers and memory analyzers.

**Model checking** is a formal verification that it's used to check if a program satisfies a given set or properties.

**Fuzzing** is a way to test the code. You run the code with random input and you check it's behavior. You try to stress the code.

# Machine learning recap

The main components are:

- **Data:** it contains information, it can be structured or not structured. Data usually contains features and attributes relevant to a specific problem
- **Model:** a model is a mathematical representation of a pattern in the data. There are many algorithms used to make prediction and classification.
- **Training:** training is the process of feeding data to a model. The data can be labeled or unlabeled.
- **Inference:** the machine learning model, once trained, makes prediction and classification on new data based on the pattern it learned during training.
*Example:* Tik-Tok decides what to show you on your specific "for you" page.

There are 3 types of machine learning:

- **Supervised learning:** uses labeled data
- **Unsupervised learning:** uses unlabeled data (and needs to create clusters on its own)
- **Reinforced learning:** creates new data as it goes.
*Example:* I have a function, I need to classify the values that the function can actually return.
*Example:* I have a game, I try to improve the way the AI plays overtime.

Main machine learning tasks:

- **Classification:** classifies data points into categories or classes based on their features. (Example: email spam detection, medical diagnosis)
- **Regression:** predicting continuous values or numerical outcomes based on input features. (*Example:* stock price prediction, demand forecasting. *Real example:* a Wallmart in Florida made big earnings by analyzing the specific requests of customers during hurricanes).
- **Clustering:** is used only in unsupervised learning. Clustering means grouping similar data points into clusters based on their characteristics and patterns. (*Example:* customer segmentation, image segmentation)
- **Anomaly detection:** analyzing the data to find if there is any data which deviated from the rest
- **Dimensionality reduction:** having less redundant data makes works easier and faster
  - **Feature selection and extraction:** is important to identify the right features needed and also to create new, more specific, features.
  - **Applications:** data visualization, feature engineering, image and signal processing, text mining and natural language.

# Why use machine learning for software analysis

Machine learning algorithms excel in analyzing large volumes of data and identifying patterns.
Program analysis without machine learning usually requires the use of manual inspection, which can be more time consuming and error prone.
We can see that in our case we have millions of lines of code so machine learning can work better than a human.
Another plus in our case is that there is tons of data related to software projects (github and other public repositories). Both the code and the metadata of a Github repo can be used by a machine learning model.

Machine learning can enhance **accuracy** and **efficiency** by identifying specific patterns and anomalies.
Another reason to prefer machine learning to a human is that a model is easier to adapt than a human can adapt.
Machine learning can make good suggestions about decision making, so it can also help the work of humans. It also opens new possibilities.
*Note:* see paper and tables on the slides about what's actually used in the industry
