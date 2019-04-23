import pandas as pd
import numpy as np
import os
import math
import subprocess


def decision_tree_learning(examples, attributes, parent examples):
    if examples is None:
        return plurality_value(parent_examples)
    elif all examples have the same classification:
        return the classification
    elif attributes is empty:
        return plurality_value(examples)
    else:
        A ←argmaxa ∈ attributes IMPORTANCE(a, examples)
        tree ← a new decision tree with root test A
        for each value vk of A do
            exs ← {e : e ∈examples and e.A = vk}
            subtree ← DECISION-TREE-LEARNING(exs, attributes − A, examples)
            add a branch to tree with label (A = vk) and subtree subtree
        return tree
        
        for vk in A:
            

    
    
# import the dataset
#
# give path to data (local or url) and column to classify on)
#
# by default, look at "heart.data" locally then remotely
def import_dataset(path = "congress_train.csv", index_col = 13):
    if os.path.exists("congress_train.csv"):
        print("Dataset: {}\nFound: Locally".format(path))
        try:
            df = pd.read_csv(path, header=0, engine='python', index_col=index_col)
            # note: engine selection as python is more stable on my machine
            # using c gives random segfaults
        except IndexError as ind:
            print(ind)
            print("Index provided: {}".format(index_col))
            exit()
        except:
            print("Failed to parse data set...")
            raise
    else:
        print("Dataset not found locally.\nDownloading dataset...")
        try:
            df = pd.read_csv(path)
        except:
            exit("Not a valid dataset URL")

        with open(path, 'w') as local_file:
            print("Saving dataset locally")
            df.to_csv(local_file)
    return df

    