from typing import *

# Given the stock prices of a company in a certain period, calculate when to buy & sell for max. profit.
# This problem is an application of divide & conquer algorithm.

stock_price = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101,
               94, 106, 101, 79, 94, 90, 97]

print("Day\tPrice")
for i in range(len(stock_price)):
    print("%i\t"%(i+1), end="")
    print("%i"%stock_price[i])

# The problem can be reduced to finding the period in which the sum of the marginal 
# profit is the largest. First we need to define a function to calculate marginal profit.
# marginal_profit[i] = stock_price[i] - stock_price[i-1]

def get_marginal_profit(stock_price: List) -> List:

    n = len(stock_price)
    marginal_profit = list()

    for i in range(1, n):
        marginal_profit.append(stock_price[i] - stock_price[i-1])

    return marginal_profit

# calculate marginal profit
marginal_profit = get_marginal_profit(stock_price)

# Next, find the maximum subarray of marginal_profit.
# Set the starting point as "left", ending point as "right", and middle point as "mid",
# there will be 3 possible situations for the maximum subarray:
# 1. Between "left" and "mid"
# 2. Between "mid+1" and "right"
# 3. Crossing "mid"

def find_max_crossing_subarray(A: List, low: int, mid: int, high:int ) -> Tuple:
    """
        This function finds the maximum subarray described in situation 3 above.
    """
    # start from mid and move leftward, find the largest sum
    left_sum = -9999
    total_sum = 0
    for i in range(mid, low-1, -1):
        total_sum += A[i]
        if total_sum > left_sum:
            left_sum = total_sum
            max_left = i

    # start from mid and move rightward, find the largest sum
    right_sum = -9999
    total_sum = 0
    for j in range(mid+1, high+1):
        total_sum += A[j]
        if total_sum > right_sum:
            right_sum = total_sum
            max_right = j

    # return the location and value of the maximum subarray
    return (max_left, max_right, left_sum + right_sum)

# Then we can proceed to the main algorithm.

def find_max_subarray(A: List, low: int, high: int) -> Tuple:
    """
        @brief:  find the maximum subarray of an unordered array.
        @params: A - list
                 low - int, starting position in A
                 high - int, ending position in A
        @retval: tuple - (low, high, sum), the location and the value of the max subarray
    """

    # base case: when the subarray only has one element, it is the maximum subarray itself
    if high == low:
        return (low, high, A[low])

    # divide the problem into two halves recursively
    mid = (low + high) // 2
    left_low, left_high, left_sum = find_max_subarray(A, low, mid)
    right_low, right_high, right_sum = find_max_subarray(A, mid+1, high)

    # merging process, compare left/right/crossing max subarrays and return the largest
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_low, left_high, left_sum)
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return (right_low, right_high, right_sum)
    else:
        return (cross_low, cross_high, cross_sum)

# It is easy to deduce that the function find_max_crossing_subarray has linear time complexity O(n),
# while the function find_max_subarray should be recursively called for less than (log2(n)+1) times,
# so the time complexity of this algorithm is O(n*log2(n)).

print("Now running the algorithm")

buy, sell, profit = find_max_subarray(
    marginal_profit, 0, len(marginal_profit)-1)
print("Buy on day {}, sell on day {}，the maximum profit is ${}."
    .format(buy+1, sell+2, profit))

# Following are some other ways to solve this problem.

# 1. Brute force (Time complexity: O(n**2))
def brute_force(marginal_profit):
    max_left, max_right = 0, 0
    max_profit = 0
    n = len(marginal_profit)
    for i in range(n):
        for j in range(i, n):
            if sum(marginal_profit[i:j]) > max_profit:
                max_left, max_right = i, j
                max_profit = sum(marginal_profit[i:j])
    return (max_left, max_right, max_profit)

# 2. Dynamic programming (Time complexity: O(n))
def dynamic_programming(marginal_profit):
    """
    Starting from 0 and moving rightward, record the current max subarray.
    For the subarray A[0:j+1]，its max subarray can be：

    1. The max subarray of A[0:j]
    2. A[i:j+1], where i belongs to [0, j+1]

    However, the max subarray of A[0:j] may be disconnected with A[j+1], 
    which makes it hard to establish a relationship between state[i] and state[i-1].
    
    Therefore, we define dp[i] to be the max subarray of marginal_profit[0:i] that ends
    with marginal_profit[i]. Then:

        dp[i] = max(dp[i-1]+marginal_profit[i], marginal_profit[i])
    
    Then we can start dynamic programming.
    """
    n = len(marginal_profit)
    low, high = 0, 0

    dp = [0 for _ in range(n)]
    dp[0] = marginal_profit[0]

    # record the starting and ending position of each subarray
    coord = [(-1, -1) for _ in range(n)]
    coord[0] = (0, 0)

    for i in range(1, n):
        temp = dp[i-1] + marginal_profit[i]
        if temp < marginal_profit[i]:
            # the maximum subarray is just marginal_profit[i] itself
            low, high = i, i
            dp[i] = marginal_profit[i]
        else:
            # the max subarray is marginal_profit[i] + dp[i-1]
            high = i
            dp[i] = temp
        coord[i] = (low, high)

    max_profit = -99999

    # find the maximum number in dp
    for i in range(n):
        if max_profit < dp[i]:
            max_profit = dp[i]
            low, high = coord[i]

    return (low, high, max_profit)

# 3. Another method with time complexity of O(n)
def iterative_find_maximum_subarray(marginal_profit):
    n = len(marginal_profit)
    max_profit = -99999
    profit = -99999
    for i in range(n):
        current_high = i

        if profit > 0:
            profit += marginal_profit[i]
        else:
            current_low = i
            profit = marginal_profit[i]

        if profit > max_profit:
            max_profit = profit
            low = current_low
            high = current_high

    return (low, high, max_profit)
