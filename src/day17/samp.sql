# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 10:51:28 2026

@author: HP
"""

CREATE TABLE students (
    id INTEGER,
    name TEXT,
    marks INTEGER
);
Insert sample data:
INSERT INTO students VALUES (1, 'Amit', 85);
INSERT INTO students VALUES (2, 'Riya', 92);
INSERT INTO students VALUES (3, 'John', 78);

SELECT * FROM students;d. Code Examples
SELECT name, marks FROM students;
