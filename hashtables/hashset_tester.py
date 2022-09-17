from myhashset import MyHashSet
from hashset_solutions202208 import Solution


solver = Solution()


print("####################")
print("Testing hashset algorithms")


# Testing containsDuplicate
print("-----")
print("Looking for duplicates in the hashset")
list1 = [1,2,3,1]
print(f"Example 1 at start: {list1}")
bool1 = solver.containsDuplicate(list1)
print(f"Does this list contain duplicates? {bool1}")
list2 = [1,2,3,4]
print(f"Example 2 at start: {list2}")
bool2 = solver.containsDuplicate(list2)
print(f"Does this list contain duplicates? {bool2}")
list3 = [1,1,1,3,3,4,3,2,4,2]
print(f"Example 3 at start: {list3}")
bool3 = solver.containsDuplicate(list3)
print(f"Does this list contain duplicates? {bool3}")


# Testing singleNumber
print("-----")
print("Looking for numbers without a duplicate in the hashset")
list1 = [2,2,1]
print(f"Example 1: {list1}")
num1 = solver.singleNumber(list1)
print(f"The single number = {num1}")
list2 = [4,1,2,1,2]
print(f"Example 2: {list2}")
num2 = solver.singleNumber(list2)
print(f"The single number = {num2}")
list3 = [1]
print(f"Example 3: {list3}")
num3 = solver.singleNumber(list3)
print(f"The single number = {num3}")

# Testing intersection
print("-----")
print("Finding intersection of 2 arrays:")
nums1 = [1,2,2,1]
nums2 = [2,2]
print(f"Intersection of {nums1} and {nums2} is {solver.intersection(nums1, nums2)}")
nums3 = [4,9,5]
nums4 = [9,4,9,8,4]
print(f"Intersection of {nums3} and {nums4} is {solver.intersection(nums3, nums4)}")


# Testing isHappy
print("-----")
n1 = 19
print(f"Is {n1} a happy number? {solver.isHappy(n1)}")
n2 = 2
print(f"Is {n2} a happy number? {solver.isHappy(n2)}")
n3 = 7
print(f"Is {n3} a happy number? {solver.isHappy(n3)}")
