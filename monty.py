# Modeling monty python game show scenario:
# Three doors, behind one is a prize. You choose one and then the
# host reveals that one of the other doors is empty, and gives you
# the option to switch doors. Should you switch?

import random

sample_size = 100000
no_switch_wins = 0
switch_wins = 0
x = [1, 2, 3]
for _ in range(sample_size):
    # no switching
    ans = random.choice(x)
    your_guess = random.choice(x)
    if ans == your_guess:
        no_switch_wins += 1

    # switching
    empty_shown = [elem for elem in x if elem != ans and elem != your_guess][0]
    your_guess = [new for new in x if new != empty_shown and new != your_guess][0]
    if ans == your_guess:
        switch_wins += 1
    
print(f"Sample size: {sample_size}")
print("Average when switching is {:.2%}.".format(switch_wins / sample_size))
print("Average when sticking with first choice is {:.2%}.".format(no_switch_wins / sample_size))
