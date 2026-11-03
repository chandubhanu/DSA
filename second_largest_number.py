"""
Challenge 1 – Find the second largest number

Press Ctrl + Shift + X.
"""

a = [12, 5, 19, 8, 25, 3]
largest=second_largest=a[0]

for num in a:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        second_largest=num
print(second_largest)