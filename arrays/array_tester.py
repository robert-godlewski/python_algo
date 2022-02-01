from array_solutions import Solution


solver = Solution()

nums1 = [1,1,0,1,1,1]
nums2 = [1,0,1,1,0,1]


print("Finding the Maximum Consecutive Numbers:")
print()
print(f"nums = {nums1}")
print(str(solver.findMaxConsecutiveOnes(nums1)))
print()
print(f"nums = {nums2}")
print(str(solver.findMaxConsecutiveOnes(nums2)))
