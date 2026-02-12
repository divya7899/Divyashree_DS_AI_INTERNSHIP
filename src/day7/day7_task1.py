# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 11:21:59 2026

@author: User
"""

name = input("Enter your name: ")
goal = input("Enter your daily goal: ")

with open("journal.txt", "a") as file:
    file.write(f"Name: {name}, Goal: {goal}\n")
