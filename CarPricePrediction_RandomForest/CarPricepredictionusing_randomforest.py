

import pandas as pd

dataset = pd.read_csv('dataset.csv')
print(dataset)


dataset = dataset.drop(['car_ID'],axis=1)

"""### *Summarize Dataset*"""

print(dataset.shape)
print(dataset.head(5))

"""### *Splitting Dataset into X & Y*
### *This X contains Both Numerical & Text Data*
"""

Xdata = dataset.drop('price',axis='columns')
numericalCols=Xdata.select_dtypes(exclude=['object']).columns
X=Xdata[numericalCols]
print(X)

Y = dataset['price']
print(Y)

"""### *Scaling the Independent Variables (Features)*"""

from sklearn.preprocessing import scale
cols = X.columns
X = pd.DataFrame(scale(X))
X.columns = cols
X

"""### *Splitting Dataset into Train & Test*"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.20,random_state=0)

"""### *Training using Random Forest*"""

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(x_train, y_train)

"""### *Evaluating Model*"""

ypred = model.predict(x_test)

from sklearn.metrics import r2_score
r2score = r2_score(y_test,ypred)
print("R2Score",r2score*100)
