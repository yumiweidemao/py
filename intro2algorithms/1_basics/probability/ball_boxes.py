import random
import math

# Suppose we're throwing balls randomly at different boxes. 
# How many times are we gonna throw so that each box contains at least a ball?

# Suppose we have b boxes, and suppose we have not missed at throw i (this is
# valid because we cannot miss at the first throw, then we just do the problem
# recursively). Now we have i-1 full boxes and b-i+1 empty boxes.
# So the probability of a successful throw is
# p = (b-i+1)/b.
# It is a GEOMETRIC DISTRIBUTION so our expectation is
# Ei = 1/p = b/(b-i+1)
# Summing the expectations up from 1 to b, we get
#               E = b*ln(b) + O(1).

# Let's prove with simulations. You can adjust the value.
number_of_boxes = 1000

"""
The following does not need to be modified.
"""

def generate_boxes(number_of_boxes):
    boxes = [0 for _ in range(number_of_boxes)]
    return boxes

def still_not_all_full(boxes):
    for box in boxes:
        if box == 0:
            return True
    return False

total_throws = 0

# Simulation starts
boxes = generate_boxes(number_of_boxes)

while still_not_all_full(boxes):
    index = random.randint(0, number_of_boxes-1)
    boxes[index] += 1
    total_throws += 1

expectation = number_of_boxes * math.log(number_of_boxes)

print("Total throws: %i" %total_throws)
print("Expectation: %.2f\n" %expectation)
print("Difference: %.2f" %(abs(expectation - total_throws)/expectation*100)+"%")
