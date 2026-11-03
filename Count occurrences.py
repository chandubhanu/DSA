"""
Challenge 2 – Count occurrences
"""

numbers = [4, 2, 7, 2, 9, 2, 5]
target = 2
count=0

for num in numbers:
    if num == target:
        count+=1

print(f"{target} appears {count} times")