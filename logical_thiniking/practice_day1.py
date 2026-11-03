"""
Challenge: Find the first repeated number
You are given a Python list:

numbers = [4, 7, 2, 9, 7, 4, 3]

Your task is to find the first number that appears again while scanning the list from left to right.
You must solve this without using set(), count(), or other built-in shortcuts.
"""

numbers = [4, 7, 2, 9, 7, 4, 3]
a=[]
for num in numbers: 
    if num not in a:
        a.append(num)
    elif num in a: 
        print(num)
        break