# List of Solutions solved in Apr 2024
class Solution:
    # Binary Search - Brute Force
    # Time Complexity = O(n)
    # Space Complexity = O(1)
    # Solved in 5 min
    def searchBrute(self, nums: list[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            else:
                i += 1
        return -1

    # Binary Search - Optimized
    # Best Time Complexity = O(1)
    # Average Time Complexity = O(logn)
    # Space Complexity = O(1)
    # Solved in 30 min - Need to practice
    def bsearch(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
        return -1

    # Sqrt(x)
    # Time Complexity = O(1)
    # Space Complexity = O(1)
    # Solved in 1 min
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)

    # Search in Rotated Sorted Array
    # Time Complexity
    # Space Complexity
    # This is a bad solution
    def rsearch(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            elif nums[mid] > target and nums[start] > target:
                start = mid + 1
            elif nums[mid] < target and nums[end] < target:
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
        return -1
