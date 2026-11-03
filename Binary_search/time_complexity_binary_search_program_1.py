"""
Coding Challenge – Your first Binary Search
"""
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 70
left=0
right=len(numbers)-1

found=False

while left<=right:
 mid=(left+right)//2    
 if numbers[mid] == target:
        found=True
        print(f"{target} found at index{mid}" )
        break
 elif numbers[mid] < target:
        left=mid+1
 else:
         right=mid-1
if not found:
    print("Target not found")



    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 70
left=0
right=len(numbers)-1

found=False

while left<=right:
 mid=(left+right)//2 
 if mid<=0:
      print("list is empty")
 elif numbers[mid] == target:
        found=True
        print(f"{target} found at index{mid}" )
        break
 elif numbers[mid] < target:
        left=mid+1
 else:
         right=mid-1
if not found:
    print("Target not found")