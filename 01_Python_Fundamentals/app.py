
# Print a welcome message
print("Hello, World!")


# Get two numbers from the user to demonstrate swapping
a = int(input("Enter first number: "))  # First number
b = int(input("Enter second number: ")) # Second number

# Display original values before swapping
print(f"Before swapping: a = {a}, b = {b}")

# Swap without a third variable using arithmetic operations
# Algorithm:
# 1. Add both numbers and store in first variable
# 2. Get first number by subtracting second from sum
# 3. Get second number by subtracting new first from sum
a = a + b 
print(a) # Step 1: Sum stored in a
b = a - b  # Step 2: Get original value of a
print(b)   # Print intermediate step
a = a - b  # Step 3: Get original value of b
print(a)   # Print final step

# Display values after swapping is complete
print(f"After swapping: a = {a}, b = {b}")


# Demonstrate even/odd number checking
# Get input from user
number = int(input("Enter a number: "))

# Use modulo operator to check if number is even or odd
# If number % 2 is 0, it's even, otherwise odd
if number % 2 == 0:
    print(f"{number} is even!")  # Print if even
else:
    print(f"{number} is odd!")   # Print if odd