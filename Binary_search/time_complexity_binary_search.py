"""
Time and Space Complexity – Level 2
"""

"""
1. O(n) – Linear Time
When input size increases, the number of operations increases proportionally.

Example:

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)
If input doubles, the number of loop executions doubles.

2. O(n²) – Quadratic Time
When input size increases, the number of operations grows approximately with the square of the input size.

Example:
numbers = [10, 20, 30, 40, 50]

for i in numbers:
    for j in numbers:
        print(i, j)

"""



"""
------------------------------------------Lesson 2 – Understanding O(1) and O(log n)--------------------------------------------
------------------------------------------Binary Search-------------------------------------------------------------------------

This will help you understand why Binary Search is much faster than Linear Search for large sorted lists.

New concept
 O(log n) – Logarithmic Time

Imagine searching for a word in a dictionary.

Would you start from the first page and check every page?

Probably not!

You would:
1. Open the middle.
2. Check whether your word comes before or after that page.
3. Ignore half of the dictionary.
4. Repeat.
This is the basic idea of Binary Search.

Before writing the code, you need to understand three important variables:
Variable	Purpose
left	Starting index of the search area
right	Ending index of the search area
mid	Middle index of the search area

The middle index is calculated using:
mid = (left + right) // 2
"""