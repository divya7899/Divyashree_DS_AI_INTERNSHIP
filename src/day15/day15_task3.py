import random

P_spam = 0.10
P_ham = 0.90

P_free_given_spam = 0.90
P_free_given_ham = 0.05

# Total probability of "Free"
P_free = (P_free_given_spam * P_spam) + (P_free_given_ham * P_ham)

# Bayes Theorem
P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("Bayesian Spam Filter Problem")
print("Theoretical Probability (Spam | Free) =", P_spam_given_free)
print()

trials = 10000
free_count = 0
spam_and_free_count = 0

for _ in range(trials):
    # Decide spam or ham
    email_type = random.choices(
        ["Spam", "Ham"],
        weights=[P_spam, P_ham]
    )[0]
    
    # Decide if "Free" appears
    if email_type == "Spam":
        has_free = random.random() < P_free_given_spam
    else:
        has_free = random.random() < P_free_given_ham
    
    if has_free:
        free_count += 1
        if email_type == "Spam":
            spam_and_free_count += 1

# Experimental Probability
exp_prob = spam_and_free_count / free_count

print("Experimental Probability (Spam | Free) =", exp_prob)
