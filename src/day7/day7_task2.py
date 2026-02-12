# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 11:40:19 2026

@author: User
"""


import csv

with open(
    r"C:\Users\HP\OneDrive\Documents\DS_AI_Intership\src\day7\students.csv",
    "r",
    encoding="utf-8-sig"
) as file:
    reader = csv.DictReader(file)

    for row in reader:
        status = row.get("Status")
        name = row.get("Name")

        if status and status.strip().lower() == "pass":
            print(name.strip())
