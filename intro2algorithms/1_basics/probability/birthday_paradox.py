import random
import math

# How many people at least should be in a room so that the probability of at
# least 2 people sharing the same birthday is exactly 0.5?

# The correct answer is 23. It changes according to the numbers of days in a year.

# Let's just do simulations. You can adjust the following values.
number_of_people = 23
days_in_a_year = 365
simulation_times = 1500

"""
The following should not be modified.
"""

def generate_people(number_of_people):
    people = [0 for _ in range(number_of_people)]
    for i in range(number_of_people):
        people[i] = random.randint(0, days_in_a_year)
    return people

def paradox_is_true(people):
    """
    Check if a list of people has at least 2 people with the same birthday.
    """
    n = len(people)
    for i in range(n-1):
        for j in range(i+1, n):
            if people[i] == people[j]:
                return True
    return False

probability = 0
for _ in range(simulation_times):
    people = generate_people(number_of_people)
    if paradox_is_true(people):
        probability += 1/simulation_times

print("Number of people: %i" %number_of_people)
print("Days in a year: %i\n" %days_in_a_year)
print("Probability: %.3f\n" %probability)
