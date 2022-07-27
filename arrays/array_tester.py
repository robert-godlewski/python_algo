from array_solutions202207 import Solution


solver = Solution()


print("####################")
print("Testing array algorithms")


# Testing duplicateZeros
arr1 = [1,0,2,3,0,4,5,0]
arr2 = [1,2,3]
print("-------")
print("Finding any 0's in the array and duplicating it")
print(f"First test original: {arr1}")
arr1 = solver.duplicateZeros(arr1)
print(f"First test solution: {arr1}")
print(f"Second test original: {arr2}")
arr2 = solver.duplicateZeros(arr2)
print(f"Second test solution: {arr2}")


# Testing merge
arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]
print("--------")
print("Merging 2 Arrays:")
print(f"Merging {arr1} and {arr2}")
arr1 = solver.merge(arr1, 3, arr2, 3)
print(f"Solution = {arr1}")
print(f"Merging [1] and []")
arr3 = solver.merge([1], 1, [], 0)
print(f"Solution = {arr3}")
print(f"Merging [0] and [1]")
arr4 = solver.merge([0], 0, arr3, 1)
print(f"Solution = {arr4}")
# Needed to use a sorting algorithm to get these 2 arrays together
arr5 = [4,5,6,0,0,0]
arr6 = [1,2,3]
print(f"Merging {arr5} and {arr6}")
arr5 = solver.merge(arr5, 3, arr6, 3)
print(f"Solution = {arr5}")

# Testing removeElement
arr1 = [3,2,2,3]
print("--------")
print("Removing numbers from arrays")
print(f"Removing 3 from {arr1}")
remaining1 = solver.removeElement(arr1, 3)
print(f"There are {remaining1} numbers left in the array")
arr2 = [0,1,2,2,3,0,4,2]
print(f"Removing 2 from {arr2}")
remaining2 = solver.removeElement(arr2, 2)
print(f"There are {remaining2} numbers left in the array")

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
