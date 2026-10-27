"""
--------------------Linear Search--------------------

linear search means searching the item one by one until we find the  item we are ooking for 
or we ran out of itmes


Here is the logic in plain English:
1. Start at the first item.
2. Compare it with the target.
3. If it matches, stop.
4. Otherwise, move to the next item.
5. Repeat until the target is found or no items remain.

[A, B, C, D, E]

Notice that the number of checks changes depending on where the target is located.
- If the target is first, we finish quickly.
- If the target is later, we do more work.
- If the target is missing, we must check every book.
"""


print("-------------Linear Search---------------")

numbers = [4, 8, 2, 9, 6]
target=9

for num in numbers:
    if num==target:
        print("Found")
        break
    else:
        print("Not found")


print("-------------Linear Search type 2---------------")

numbers = [4, 8, 2, 9, 6]
target=9
is_found=False
for i in range(len(numbers)):
    if numbers[i]==target:
        print("Found")
        is_found=True
        break
    if is_found==False:
     print("Not Found")

    