"""
Test 1 – Target at the beginning
"""

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 10
found=False
left=0
right=len(numbers)-1

while left<=right:
    mid=(left+right)//2
    if numbers[mid]==target:
        found=True
        print(f"{target} is found at {mid}")
        break
    elif numbers[mid]>target:
        right=mid-1
    else:
        left=mid+1
    
        