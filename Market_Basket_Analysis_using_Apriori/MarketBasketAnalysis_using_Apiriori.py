
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""### Importing the dataset"""

dataset = pd.read_csv('dataset.csv')
print(dataset.shape)
print(dataset.head(5))

"""### Data Pre-Processing"""

transactions = []
for i in range(0, 7500):
  transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])
print(transactions)

"""### Training APRIORI"""

from apyori import apriori
rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

"""### Result"""

results = list(rules)
print(results)

"""### Results in Dataframe"""

lhs         = [tuple(result[2][0][0])[0] for result in results]
rhs         = [tuple(result[2][0][1])[0] for result in results]
supports    = [result[1] for result in results]
confidences = [result[2][0][2] for result in results]
lifts       = [result[2][0][3] for result in results]
resultsinDataFrame = pd.DataFrame(zip(lhs, rhs, supports, confidences, lifts), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])
print(resultsinDataFrame)
