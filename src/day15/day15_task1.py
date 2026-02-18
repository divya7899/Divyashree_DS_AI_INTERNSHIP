# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 10:27:44 2026

@author: HP
"""
import random

actions = ["Click", "Scroll", "Exit"]
trials = 10000
click_at_least_once = 0

for _ in range(trials):
    action1 = random.choice(actions)
    action2 = random.choice(actions)
    
    if action1 == "Click" or action2 == "Click":
        click_at_least_once += 1

exp_click_prob = click_at_least_once / trials

theo_click_prob = 1 - (4 / 9)

print("Customer Click Problem")
print("Theoretical Probability =", theo_click_prob)
print("Experimental Probability =", exp_click_prob)
print()

dice_trials = 10000
count_sum_7 = 0

for _ in range(dice_trials):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    
    if d1 + d2 == 7:
        count_sum_7 += 1

exp_dice_prob = count_sum_7 / dice_trials

theo_dice_prob = 1/6

print("Dice Sum = 7 Problem")
print("Theoretical Probability =", theo_dice_prob)
print("Experimental Probability =", exp_dice_prob)
