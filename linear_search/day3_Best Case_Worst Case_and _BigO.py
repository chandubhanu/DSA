"""
Lesson 4:Best Case, Worst Case, and Big O
You have 5 books:
A  B  C  DE

You want to find book C.

You check the books one by one.
- Best case: The target is first. You need only 1 check.
- Worst case: The target is last. You need 5 checks.
- Target missing: You also need 5 checks because you must check every book.
2. Understand the difference
Situation	Meaning	Checks for 5 books
Best case	Least work	1
Worst case	Most work	5
Target missing	Check every book	5
"""

print("----linear search proram 1----O(n)")

a=[4,8,2,9,6]
is_found=False
target=9
for num in a:
    if num==target:
        is_found=True
        print("Found")
        break

#worst case
numbers = [4, 8, 2, 9, 6]
target = 7

found = False

for number in numbers:
    if number == target:
        found = True
        break

print(found)


