"""
Lesson 10: Find the Position of a Number
Previously, our program answered: “Did we find the number?”


Quick revision
- Python list indexes start at 0.
- The first element has index 0.
- The second element has index 1.
- The sixth element has index 5.
- Number of elements and last index are different: 6 elements means the last index is 5.
Remember this trick: Last index = number of elements − 1.


Index vs. Position
In Lesson 11, we practised finding the index and position of a number. Now we'll practise both together.
Position = Index + 1.
Number	Index	Position
10	0	1st
20	1	2nd
30	2	3rd
40	3	4th
50	4	5th
"""

numbers = [4, 8, 12, 16, 20]
target = 12

for index in range(len(numbers)):
    if numbers[index] == target:
        print(index)
        break

print("-------Program 1-----------")
numbers = [4, 8, 2, 9, 6]
target = 9
found=False
for i in range(len(numbers)):
    if numbers[i] == target:
        found=True
        break               
print(found)

print("-------Proram 2-----------")
numbers = [4, 8, 2, 9, 6]
target = 7
found=False

for num in numbers:
    if num==target:
        found=True
        break
print(found)


print("-------Proram 3-----------")
numbers = [12, 5, 19, 8, 25]
target = 8
found=False
for i in range(len(numbers)):
    if numbers[i] == target:
        found=True
        print(i)
        break               


print("-------Proram 4-----------")
numbers = [12, 5, 19, 8, 25]
target = 7

for num in numbers:
    if num==target:
      print("found")
      break
else:
        print("not found")

print("-------Proram 5-----------")
numbers = [12, 5, 19, 8, 25]
target = 8

for i in range(len(numbers)):
    if numbers[i]==target:
      print("found")
      print(i)
      break
else:
        print("not found")

print("-------Proram 6-----------")
numbers = [10, 20, 30, 20, 40]
target = 20

for i in range(len(numbers)):
    if numbers[i]==target:
        print(i)

print("-------Proram 7-----------")
#Challenge 6 — Count occurrences
numbers = [10, 20, 30, 20, 40, 20]
target = 20
count=0
for i in range(len(numbers)):
    if numbers[i]==target:
        count+=1

print(count)


print("-------Proram 8-----------")
#Challenge 7: Find the largest number
numbers = [12, 5, 19, 8, 25, 3]
largest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
print(largest)


print("-------Proram 9-----------")
#Challenge 8 — Find the smallest number
numbers = [12, 5, 19, 8, 25, 3]
smallest=numbers[0]
for num in numbers:
    if num<smallest:
        smallest=num
print(smallest)


print("-------Proram 10-----------")
#Challenge 9 — Find the second largest number
numbers = [12, 20, 15]
largest=numbers[0]
second_largest=0

for i in range(len(numbers)):
    if numbers[i]>largest:
        second_largest=largest
        largest=numbers[i]
    elif numbers[i]>second_largest and numbers[i]!=largest:
        second_largest=numbers[i]
print(second_largest)