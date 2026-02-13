# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 14:44:49 2026

@author: HP
"""

import pandas as pd


df = pd.read_excel("customer_orders.xlsx")


print("Before normalization:")
print(df["Location"].unique())



df["Location"] = df["Location"].str.strip().str.title()

print("\nAfter normalization:")
print(df["Location"].unique())
