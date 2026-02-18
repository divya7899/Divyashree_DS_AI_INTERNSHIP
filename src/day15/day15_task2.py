import random

trials = 10000
count_success = 0
for _ in range(trials):
    coin = random.choice(["H", "T"])
    die = random.randint(1, 6)
    
    if coin == "H" and die == 6:
        count_success += 1
# Experimental Probability
exp_independent_prob = count_success / trials

# Theoretical Probability
theo_independent_prob = (1 / 2) * (1 / 6)
print("Independent Events (Heads AND 6)")
print("Theoretical Probability =", theo_independent_prob)
print("Experimental Probability =", exp_independent_prob)
print()

marble_trials = 10000
both_red_count = 0

for _ in range(marble_trials):
    marbles = ["Red"] * 5 + ["Blue"] * 5
    first = random.choice(marbles)
    marbles.remove(first)
    second = random.choice(marbles)
    
    if first == "Red" and second == "Red":
        both_red_count += 1

# Experimental Probability
exp_dependent_prob = both_red_count / marble_trials

# Theoretical Probability
theo_dependent_prob = (5 / 10) * (4 / 9)
print("Dependent Events (Both Red Marbles)")
print("Theoretical Probability =", theo_dependent_prob)
print("Experimental Probability =", exp_dependent_prob)
