import random
import math

# Suppose we have 100 candidates, among which we want to hire only one to
# be our assistant. We want to know how many times in average that we hire
# a candidate.

def generate_candidates(n):
    """
    Generate a list of random integers ranging from 0-n, representing the
    qualifications of each interviewee.
    """
    candidates = [0 for _ in range(n)]
    for i in range(n):
        candidates[i] = random.randint(0, n)
    return candidates

def stupid_hire_assistant(candidates):
    """
    Interview each candidate, if he/she is the best candidate, hire him/her;
    if anyone better appears, fire the current assistant and hire a new one.
    Returns the total number of hires during this process.
    """

    # candidate 0 is a least-qualified dummy candidate
    best_candidate = 0
    hire_times = 0

    # interview each candidate
    for candidate in candidates:
        if candidate > best_candidate:
            # candidate is best, hire candidate
            best_candidate = candidate
            hire_times += 1

    return hire_times, best_candidate


# Suppose the probability of Candidate number i being hired is Xi. Before
# Candidate #i, there are i-1 candidates, so there is a probability of
# 1/i that Candidate i is the best and is hired. So the total expectation of 
# hires is equal to the sum of (1/i) where i is from 1 to n, which is 
# approximately equal to ln(n).  (Taylor Series)

# Let's use simulations to see that.
n = 1000                # number of candidates
simulation_times = 100  # number of simulations

# Use the average value of the simulations.
average_hire_times = 0

for i in range(simulation_times):
    # Generate 1000 candidates
    candidates = generate_candidates(n)

    # Hire them using our predefined process
    hire_times, best_candidate = stupid_hire_assistant(candidates)

    average_hire_times += hire_times/simulation_times

# Compare with the expectation ln(n)
expectation = math.log(n)
print("Expected number of hires: %.2f" %expectation)
print("Actual number of hires: %.2f" %average_hire_times)

# ------------------------------------------------------------------------
print("\n--------------------------------------------------\n")
# ------------------------------------------------------------------------

# In reality, we cannot hire and then fire people. Suppose now we only have
# one chance to hire one candidate. How to hire the best candidate?

# We can first determine a best candidate from i = 1 to k, 
# then from i = k+1 to n, we hire the candidate that is better than the best.
# If no candidate is better, we just hire the last candidate, Candidate #n.

# After some calculations (can be found on Chap.5 of Intro to Algorithms),
# we find that the best value for k is
# k = n/e.
# At this value of k, we have a probablity of hiring the best candidate of
# P = 1/e.

# Let's use simulations to see that.
n = 1000                    # number of candidates
simulation_times = 100      # number of simulations

# The final result
average_probability = 0

# Simulation begins
for _ in range(simulation_times):

    best_candidate = 0

    candidates = generate_candidates(n)

    # lower bound k = n/e, determine a best candidate
    for i in range(int(n/math.e)):
        if candidates[i] > best_candidate:
            best_candidate = candidates[i]

    # Run through the rest to see the first better candidate
    for i in range(int(n/math.e), n):
        if candidates[i] > best_candidate:
            # Succeed only if the best is hired
            if candidates[i] == max(candidates):
                average_probability += 1/simulation_times
            break


print("Average probablity: %.4f" %average_probability)
print("Expected probablity: %.4f" %math.exp(-1))
