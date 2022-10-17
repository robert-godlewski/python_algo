from binary_search_solutions import Solution


solver = Solution ()


print("####################")
print("Testing binary search algorithms")

# Testing search
print("-------")
nums1 = [-1,0,3,5,9,12]
target1 = 9
print(f"Finding {target1} in {nums1}")
in1 = solver.search(nums1, target1)
print(f"The index is {in1}")
nums2 = [-1,0,3,5,9,12]
target2 = 2
print(f"Finding {target2} in {nums2}")
in2 = solver.search(nums2, target2)
print(f"The index is {in2}")

# Testing mySqrt
print("-------")
x1 = 4
sqrx1 = solver.mySqrt(x1)
print(f"The Sqare Root of {x1} = {sqrx1}")
x2 = 8
sqrx2 = solver.mySqrt(x2)
print(f"The Square Root of {x2} = {sqrx2}")

# Testing guessNumber
print("-------")
print("Skiped")

# Testing search
print("-------")
nums = [4,5,6,7,0,1,2]
target1 = 0
print(f"Finding {target1} in {nums}:")
index1 = solver.search(nums, target1)
print(index1)
target2 = 3
print(f"Finding {target2} in {nums}:")
index2 = solver.search(nums, target2)
print(index2)
print(f"Finding 0 in [1]:")
index3 = solver.search([1], 0)
print(index3)

