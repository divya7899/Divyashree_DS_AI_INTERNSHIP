# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 12:24:17 2026

@author: HP
"""

import matplotlib.pyplot as plt


categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Create first subplot 
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Sales")

# Create second subplot
months = [1, 2, 3, 4, 5]
revenue_trend = [200, 250, 300, 350, 400]

plt.subplot(1, 2, 2)
plt.plot(months, revenue_trend)
plt.title("Revenue Trend Over Time")
plt.xlabel("Month")
plt.ylabel("Revenue")


plt.tight_layout()


plt.show()
