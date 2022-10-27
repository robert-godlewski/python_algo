from array_solutions202207 import Solution


solver = Solution()


print("####################")
print("Testing array algorithms")


# Testing duplicateZeros
print("-------")
def duplicateZerosTest(arr: list[int]) -> None:
    print("Finding any 0's in an array and duplicating it them")
    print(f"Original = {arr}")
    arr_dup = solver.duplicateZeros(arr)
    print(f"Duplicated = {arr_dup}")

duplicateZerosTest([1,0,2,3,0,4,5,0])
duplicateZerosTest([1,2,3])


# Testing merge
print("--------")
def mergeArrTest(arr1: list[int], m: int, arr2: list[int], n: int) -> None:
    print(f"Merging {arr1} and {arr2}")
    merged_arr = solver.merge(arr1, m, arr2, n)
    print(merged_arr)

mergeArrTest([1,2,3,0,0,0], 3, [2,5,6], 3)
mergeArrTest([1], 1, [], 0)
mergeArrTest([0], 0, [1], 1)
mergeArrTest([4,5,6,0,0,0], 3, [1,2,3], 3)

# Testing removeElement
print("--------")
def removeElementTest(arr: list[int], num: int) -> None:
    print(f"Removing {num} from {arr}")
    rem_arr = solver.removeElement(arr, num)
    print(f"Remaining numbers = {rem_arr}")

removeElementTest([3,2,2,3], 3)
removeElementTest([0,1,2,2,3,0,4,2], 2)

# Testing removeDuplicates
print("--------")
def removeDuplicatesTest(arr: list[int]) -> None:
    print(f"Removing duplicates in {arr}")
    remain = solver.removeDuplicates(arr)
    print(f"Remaining values = {remain}")

removeDuplicatesTest([1,1,2])
removeDuplicatesTest([0,0,1,1,1,2,2,3,3,4])

'''
nums1 = [1,1,0,1,1,1]
nums2 = [1,0,1,1,0,1]

print("\nFinding the Maximum Consecutive Numbers:")
print_debugging(nums1, solver.findMaxConsecutiveOnes(nums1))
print_debugging(nums2, solver.findMaxConsecutiveOnes(nums2))

nums3 = [12,345,2,6,7896]
nums4 = [555,901,482,1771]

print("\nFinding the total amount of even numbered digits:")
print_debugging(nums3, solver.findNumbers(nums3))
print_debugging(nums4, solver.findNumbers(nums4))

nums5 = [-4,-1,0,3,10]
nums6 = [-7,-3,2,3,11]

print("\nFinding the squares and sorting them in order:")
print_debugging(nums5, solver.sortedSquares(nums5))
print_debugging(nums6, solver.sortedSquares(nums6))

nums7 = [1,0,2,3,0,4,5,0]

print("\nFinding and inserting duplicate 0's in a list:")
print_debugging(nums7, solver.duplicateZeros(nums7))

nums8 = [1,2,3,0,0,0]
nums9 = [2,5,6]
nums10 = [1]
nums11 = list()
nums12 = [0]
nums13 = [2,0]

print("\nMerging 2 lists together:")
print(f"nums1 = {nums8}, m = 3, nums2 = {nums9}, n = 3")
print(solver.merge(nums8, 3, nums9, 3))
print(f"nums1 = {nums10}, m = 1, nums2 = {nums11}, n = 0")
print(solver.merge(nums10, 1, nums11, 0))
print(f"nums1 = {nums12}, m = 0, nums2 = {nums10}, n = 1")
print(solver.merge(nums12, 0, nums10, 1))
print(f"nums1 = {nums13}, m = 1, nums2 = {nums11}, n = 1")
print(solver.merge(nums13, 0, nums10, 1))

nums14 = [3,2,2,3]
val1 = 3
nums15 = [0,1,2,2,3,0,4,2]
val2 = 2

print("\nDeleting a number from the array:")
print(f"nums = {nums14}, val = {val1}")
print(solver.removeElement(nums14, val1))
print(f"nums = {nums15}, val = {val2}")
print(solver.removeElement(nums15, val2))
'''
