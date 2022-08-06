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
