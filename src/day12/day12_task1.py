# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 12:13:51 2026

@author: HP
"""

import matplotlib.pyplot as plt

# Data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]

# Scatter plot (distinct, unconnected points)
plt.scatter(study_hours, scores)

# Labels and title for clarity
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")
plt.title("Study Hours vs Exam Scores")

# Display plot
plt.show()
