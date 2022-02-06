from array_solutions import Solution


solver = Solution()


def print_debugging(original, solution):
    print(str(original))
    print(str(solution))


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
