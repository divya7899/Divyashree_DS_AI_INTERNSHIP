# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 11:30:48 2026

@author: HP
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\sqllite\sample.db")
df = pd.read_sql_query("SELECT * FROM students", conn)
print(df)
