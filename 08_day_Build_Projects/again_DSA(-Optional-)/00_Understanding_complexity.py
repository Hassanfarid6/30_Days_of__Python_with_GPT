# 1. Understanding Complexity

# Complexity analysis is the foundation of algorithm design. It helps you evaluate how 
# efficient an algorithm is as the input size grows.

# Time Complexity

# Definition: Time complexity measures how the runtime of an algorithm scales with the 
# size of the input (denoted as n). It’s expressed using Big-O notation, which describes 
# the worst-case upper bound of the algorithm’s growth rate.

# Key Concepts:

# O(1): Constant time. The runtime doesn’t change with input size (e.g., accessing an array
#  element by index).

# O(n): Linear time. Runtime grows proportionally with input size (e.g., looping through an
#  array once).

# O(log n): Logarithmic time. Runtime grows slowly because the problem size is halved at each
#  step (e.g., binary search).

# O(n log n): Linearithmic time. Common in efficient sorting algorithms like Merge Sort.

# O(n²): Quadratic time. Runtime grows with the square of the input size (e.g., nested loops in
#  Bubble Sort).

# How to Analyze:

# Identify the basic operations (e.g., comparisons, assignments).
# Count how many times these operations run as a function of n.
# Simplify to the dominant term, ignoring constants and lower-order terms.
# Example: Finding the maximum element in an array:
    
arr = [1,2,3,4,5,6,8,7,10,9]
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# print(find_max(arr))
# num = find_max(arr)
# print(num)

# Operations: One comparison per element.
# Count: n comparisons for an array of size n.
# Time Complexity: O(n).



def find_maximum(arr):
    max_val = arr[0]          # O(1) space, one variable
    for num in arr:           # Loops n times: O(n) time
        if num > max_val:     # 1 comparison per loop
            max_val = num     # Updates max_val if needed
    return max_val           # Returns the result

# Test it
array = [3, 1, 4, 1, 5, 9, 2]
# print(find_maximum(array))       # Output: 9

# Time Complexity: O(n) - scales linearly with array size
# Space Complexity: O(1) - uses only one extra variable

# Space Complexity

# Definition: Space complexity measures how much additional memory an algorithm uses as the input
#  size grows, excluding the input itself (auxiliary space).

# Key Concepts:

# O(1): Constant space. Uses a fixed amount of memory (e.g., a few variables).

# O(n): Linear space. Memory grows with input size (e.g., creating a new array of size n).

# O(log n): Logarithmic space. Common in recursive algorithms due to the call stack.

# How to Analyze:
# Identify extra data structures (e.g., arrays, recursion stack).
# Determine how their size scales with n.
# Example: The find_max function above:
# Extra Space: One variable (max_val).
# Space Complexity: O(1).