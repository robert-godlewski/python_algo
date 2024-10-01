# Solutions solved in October 2024
class Solution:
    # Leetcode Sort Array - try to get it with O(nlogn) time - Need to practice
    # Best Time Solution = O(1)
    # Time Solution = O(nlogn)
    # Space Solution = O(n)
    # Solved in 30 min
    def sortArray(self, nums: list[int]) -> list[int]: 
        if len(nums) > 1:
            pivot = len(nums)//2
            left = self.sortArray(nums[0:pivot])
            right = self.sortArray(nums[pivot:])
            i = 0
            j = 0
            n = 0
            while i < len(left) and j < len(right) and n < len(nums):
                if left[i] <= right[j]:
                    nums[n] = left[i]
                    i += 1
                else: 
                    # left[i] > right[j]
                    nums[n] = right[j]
                    j += 1
                n += 1
            while i < len(left) and n < len(nums):
                nums[n] = left[i]
                i += 1
                n += 1
            while j < len(right) and n < len(nums):
                nums[n] = right[j]
                j += 1
                n += 1
        return nums