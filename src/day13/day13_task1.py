# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 11:15:03 2026

@author: HP
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

df=pd.read_csv("housing.csv")

plt.figure()
sns.histplot(df['Price'], kde=True, bins=30)
plt.title("Distribution of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

price_skewness=skew(df['Price'])
price_kurtosis=kurtosis(df['Price'])
print("skewness:",price_skewness)
print("kurtosis:",price_kurtosis)

plt.figure()
sns.countplot(x='City',data=df)
plt.title("count of houses by city")
plt.xlabel("City")
plt.ylabel("Number of Houses")
plt.xticks(rotation=45)
plt.show()