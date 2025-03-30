# Reversed The String
# _____________________________________________________________



# Explanation
# [start:stop:step]
# s[::-1] is a slicing technique that reverses the string.
# The slicing technique is a powerful tool in Python that allows you to extract a subset 
# of a string, list, or any other iterable data structure.
# The slicing technique has the following syntax: [start:stop:step].
# The start parameter specifies the starting index of the slice.
# The stop parameter specifies the ending index of the slice.
# The step parameter specifies the step size of the slice.
# In this case, the step size is -1, which means the slice is reversed.
# Therefore, s[::-1] reverses the string s.
# For example, if s = "hello", then s[::-1] returns "olleh". 

# _____________________________________________________________
# more ways to achive same result
# _____________________________________________________________

def Reverse(s):
#          s[start: stop :step]
    return s[::-1]

print(Reverse("hello"))
# Example 1
def solution1(string):
    newstring = ""
    letter = len(string) - 1
    for x in string:
        x = string[letter]
        newstring = newstring + x
        letter = letter -1 
    return newstring

# print(solution1("hello"))
# Example 2
def solution2(s):
    return ''.join(reversed(s))
# print(solution2("hello"))

# Example 3
def solution3(s):
    return ''.join(s[i] for i in range(len(s)-1, -1, -1))
print(solution3("hello ALI"))

# Example 4
solution4 = lambda s: s[::-1]
print(solution4("hello hassan"))


# you can use ai to explain the code