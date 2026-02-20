# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 12:05:25 2026

@author: HP
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

np.random.seed(42)

# Normal Distribution (Human Heights)
heights = np.random.normal(loc=170, scale=10, size=1000)

# Right-Skewed Distribution (Household Income)
income = np.random.exponential(scale=50000, size=1000)

# Left-Skewed Distribution (Easy Exam Scores)
scores = 100 - np.random.exponential(scale=10, size=1000)

# Store in DataFrame
data = {
    "Human Heights (Normal)": heights,
    "Household Income (Right-Skewed)": income,
    "Exam Scores (Left-Skewed)": scores
}

plt.figure(figsize=(15, 4))

for i, (title, values) in enumerate(data.items(), 1):
    plt.subplot(1, 3, i)
    sns.histplot(values, kde=True, bins=30)
    
    mean = np.mean(values)
    median = np.median(values)
    
    plt.axvline(mean, linestyle="--", label=f"Mean = {mean:.2f}")
    plt.axvline(median, linestyle="-", label=f"Median = {median:.2f}")
    
    plt.title(title)
    plt.legend()

plt.tight_layout()
plt.show()


for name, values in data.items():
    mean = np.mean(values)
    median = np.median(values)
    
    if mean > median:
        skew = "Right-Skewed"
    elif mean < median:
        skew = "Left-Skewed"
    else:
        skew = "Normal"
        
    print(f"{name}")
    print(f"Mean   = {mean:.2f}")
    print(f"Median = {median:.2f}")
    print(f"Distribution Type: {skew}")
    print("-" * 40)