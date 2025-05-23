# -*- coding: utf-8 -*-
"""House price prediction using Linear Regression

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RDk3rxFgiMCrh8WN8gd76-I4yBJel5gH
"""

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/bcbarsness/machine-learning/refs/heads/master/USA_Housing.csv')
df.head()

df.drop('Address',axis=1,inplace=True)

df.head()

df.columns

!pip install

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']] = scaler.fit_transform(df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']])

df.head()

from sklearn.model_selection import train_test_split


X = df.drop('Price',axis=1)
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train,y_train)
lr.score(X_test,y_test)

from sklearn.metrics import r2_score

y_preds = lr.predict(X_test)

r2_score(y_test, y_preds)

