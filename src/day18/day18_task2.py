# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 22:43:47 2026

@author: HP
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:/sqllite/internship.db")

query = """
SELECT
    interns.name AS intern_name,
    interns.track,
    mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
"""

df = pd.read_sql_query(query, conn)
print(df)

conn.close()