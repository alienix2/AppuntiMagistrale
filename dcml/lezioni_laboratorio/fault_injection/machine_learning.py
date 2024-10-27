"""
In this lab we are working with a dataset that we will divide into Train and Test sets.
We will use the Train set to train a Machine Learning model and then we will test it on the Test set. We will skip
the validation set for simplicity in this case.
We will chose a classifier, then we will train it and test on some matrics.
We will need to split the label from the rest of the data because of the way the libraries are implemented in python.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

if __name__ == "__main__":
    # 0 load dataset (pandas and numpy libraries)
    my_data = pd.read_csv("labelled_dataset.csv")

    # 0.1 drop the date and time colums cause it is not useful
    my_data = my_data.drop(columns=["datetime", "time"], axis=1)

    # 0.2 manage the future splitting
    label_obj = my_data["label"]
    data_obj = my_data.drop("label", axis=1)
    print(my_data.head())
    print(label_obj.head())
    print(data_obj.head())

    # 1 split the dataset
    train_data, test_data, train_label, test_label = train_test_split(
        data_obj, label_obj, test_size=0.4, random_state=19
    )
    print(train_data)

    # 2 and 3 choose the classifier and train it
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(train_data, train_label)

    # 4 test the classifier
    predictions = clf.predict(test_data)
    print(predictions)

    acc_score = accuracy_score(test_label, predictions)
    print(acc_score)

    tn, fp, fn, tp = confusion_matrix(test_label, predictions).ravel()

    print(
        "True Negative: "
        + str(tn)
        + " False Positive: "
        + str(fp)
        + " False Negative: "
        + str(fn)
        + " True Positive: "
        + str(tp)
    )
