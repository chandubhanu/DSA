numbers = [3, 8, 2, 9]
target = 8

found = False

for number in numbers:
    if number == target:
        found = True
        break

print(found)