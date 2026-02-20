# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 12:27:15 2026

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

population = np.random.exponential(scale=50, size=10000)

sample_means = []

for _ in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(sample.mean())

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(population, bins=40, kde=True)
plt.title("Original Skewed Population Data")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
sns.histplot(sample_means, bins=30, kde=True)
plt.title("Distribution of Sample Means (CLT)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()