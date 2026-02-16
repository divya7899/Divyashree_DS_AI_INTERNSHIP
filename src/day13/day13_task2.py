# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 12:36:47 2026

@author: HP
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("housing_bivariate.csv")
df.head()

#scatter plot price vs square footage
plt.figure()
sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.title("Price vs Square Footage")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()
print("Observation (Scatter Plot):")
print("As SquareFootage increases, Price seems to increase.\n")

#boxplot
plt.figure()
sns.boxplot(x="City", y="Price", data=df)
plt.title("Price Distribution by City")
plt.xlabel("City")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.show()
print("Boxplot Observation:")
print("As we compare different cities, Price seems to change from city to city.\n")

