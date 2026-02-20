# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 12:05:28 2026

@author: HP
"""

import numpy as np
import pandas as pd

scores = [65, 70, 72, 68, 75, 78, 74, 69, 71, 300]

df = pd.DataFrame({"Score": scores})

mu = df["Score"].mean()
sigma = df["Score"].std()

print(f"Mean (μ): {mu}")
print(f"Standard Deviation (σ): {sigma}")

df["z_score"] = (df["Score"] - mu) / sigma
print(df)

# Identify outliers where absolute Z-score is greater than 3
outliers = df[abs(df["z_score"]) > 3]

print("Statistical Outliers (|Z| > 3):")
print(outliers)