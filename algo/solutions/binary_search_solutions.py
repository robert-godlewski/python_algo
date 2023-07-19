# Binary Solutions solved in October 2022
class Solution:
    # Solution in 15 min for both search solutions
    # O(n) time solution
    def searchIritive(self, nums: list[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return -1
            else:
                i += 1

    # O(log n) time solution
    def searchIndex(self, nums: list[int], target: int, index=0) -> int:
        if index >= len(nums):
            return -1
        if nums[index] == target:
            return index
        elif nums[index] > target:
            return -1
        else:
            return self.searchIndex(nums, target, index+1)

    # Solved in 5 min
    # O(1) time
    def mySqrt(self, x: int) -> int:
        # Simple Solution but not allowed in leetcode
        return int(x**0.5)

    # Didn't quite understand how this works - guess(i) is too vague and untestable without api
    # Brute force way
    def guessNumber(self, n: int) -> int:
        for i in range(1, n):
            if guess(i) == 0:
                return i
        return n

    # Similar to searchIndex
    def search(self, nums: list[int], target: int, index=0) -> int:
        if index >= len(nums):
            return -1
        if nums[index] == target:
            return index
        else:
            return self.search(nums, target, index+1)
