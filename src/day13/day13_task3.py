# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 14:25:22 2026

@author: HP
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("housing_bivariate.csv")

# Correlation matrix (FIXED)
corr_matrix = df.corr(numeric_only=True)
print(corr_matrix)

# Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Boxplot for outliers
plt.figure()
sns.boxplot(y=df["Price"])
plt.title("Boxplot of Housing Prices")
plt.ylabel("Price")
plt.show()

# Observation
print("Observation:")
print("SquareFootage and Price show a strong positive correlation.")
print("The boxplot shows a few high-price outliers.")
