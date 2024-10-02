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

    # Leetcode Search a 2D Matrix II
    # Time Complexity = O(nlogn)
    # Space Complexity = O(n)
    # Solved in 20 min
    # Binary Search on each line of the matrix
    def _binarySearchLine(self, matrix: list[list[int]], target: int, index: int) -> bool:
        left = 0
        right = len(matrix[index])-1
        while left <= right:
            mid = (left+right)//2
            if matrix[index][mid] == target:
                return True
            elif matrix[index][mid] < target:
                left = mid+1
            elif matrix[index][mid] > target:
                right = mid-1
        return False

    # Main solution
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if len(matrix) > 0:
            i = 0
            while i < len(matrix):
                if target >= matrix[i][0] and target <= matrix[i][len(matrix[i])-1]:
                    temp = self._binarySearchLine(matrix, target, i)
                else:
                    temp = False
                if temp:
                    return True
                i += 1
        return False
