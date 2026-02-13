# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 12:21:57 2026

@author: HP
"""

import matplotlib.pyplot as plt

# Define data
months = [1, 2, 3, 4, 5]
revenue = [2000, 4500, 4000, 7500, 9000]

# Create line plot
plt.plot(months, revenue)

# Add title and labels
plt.title("Monthly Revenue Growth")
plt.xlabel("Month")
plt.ylabel("Revenue in USD")

# Show the plot
plt.show()
