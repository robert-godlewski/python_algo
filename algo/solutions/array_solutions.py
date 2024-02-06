# Array Solutions Jan 2024
# Grabbing the sorting algorithms to use
from algo.datastructures.sorting_templates import *


# Got from the Easy Collection from the Top Interview Questions group
class Solution:
    def __init__(self) -> None: pass

    # Removed Duplicates from Sorted Array
    # Space Complexity = O(1)
    # Time Complexity = O(n)
    # Solved in 10 min - for some reason Leetcode is not accepting this
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
                # nums.append('_')
                k += 1
            # elif nums[i] == '_': break
            else:
                i += 1
        print(f'Remaining values = {nums}')
        return k

    # Best Time to Buy and Sell Stock II
    # Space Complexity = O(1)
    # Time Complexity = O(n)
    # Solved in 15 min
    def maxProfit(self, prices: list[int]) -> int: 
        profit = 0
        i = 0
        buy = -1
        while i < len(prices):
            # print(f'current profit = {profit}')
            # if buy >= 0: print(f'seeing if we should sell on day {i+1}')
            # else: print(f'seeing if we should buy on day {i+1}')
            if buy < 0 and i+1 < len(prices) and prices[i] < prices[i+1]:
                buy = prices[i]
                # print(f'bought on day {i+1} for {buy}')
            elif buy >= 0 and buy < prices[i]:
                if i+1 < len(prices) and prices[i] < prices[i+1]:
                    # Not worth selling right now
                    pass
                else:
                    # i+1 <= len(prices) and or prices[i] > prices[i+1]:
                    # We need to sell
                    # print(f'selling on day {i+1} for {prices[i]}')
                    profit += prices[i] - buy
                    # print(f'{profit-prices[i]+buy} + ({prices[i]} - {buy}) = {profit}')
                    buy = -1
            i += 1
        return profit

    # Rotate Array
    # Space Complexity = O(1)
    # Time Complexity = O(n)
    # Solved in 10 minutes
    # For leetcode - Do not return anything, modify nums in-place instead.
    # def rotate(self, nums: list[int], k: int) -> None:
    def rotate(self, nums: list[int], k: int) -> list[int]:
        while k > 0:
            # print(f'Current nums = {nums}')
            # print(f'k = {k}')
            temp = nums.pop(len(nums)-1)
            nums.insert(0,temp)
            k -= 1
        # Don't return when submitting to leetcode
        return nums

    # Contains Duplicate
    # Space Complexity = O(n)
    # Time Complexity = O(n)
    # Solved in 15 min
    def containsDuplicate(self, nums: list[int]) -> bool:
        indexer = {}
        for num in nums:
            index = str(num)
            if index in indexer:
                indexer[index] += 1
            else:
                indexer[index] = 1
        for val in indexer.values():
            if val > 1:
                return True
        return False

    # Single Number
    # Space Complexity = O(n)
    # Time Complexity = O(n)
    # Solved in 10 min
    def singleNumber(self, nums: list[int]) -> int: 
        indexer = {}
        for num in nums:
            index = str(num)
            if index in indexer:
                indexer[index] += 1
            else: 
                indexer[index] = 1
        for key, val in indexer.items():
            if val == 1:
                return int(key)
        return 0

    # Intersection of 2 Arrays 2
    # Space Complexity = O(k)
    # Time Complexity = O(n+k)
    # Solved in 20 min
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]: 
        # Need to actually write out a sorting function here
        nums1 = countingSort(nums1)
        nums2 = countingSort(nums2)
        # nums is the intersection of nums1 and nums2
        nums = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                nums.append(nums1[i])
                i += 1
                j += 1
        return nums
    
    # Plus One
    # Space Complexity = O(n)
    # Time Complexity = O(n)
    # Solved in 20 min
    def plusOne(self, digits: list[int]) -> list[int]: 
        num_str = ''
        for digit in digits:
            num_str += str(digit)
        num = int(num_str)
        num += 1
        new_num_str = str(num)
        new_num = list(new_num_str)
        digits = []
        for digit in new_num:
            digits.append(int(digit))
        return digits

    # Move Zeroes
    # Space Complexity = O(1)
    # Time Complexity = O(n)
    # Solved in 10 min
    # For leetcode: Do not return anything, modify nums in-place instead.
    # def moveZeroes(self, nums: list[int]) -> None:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        i = 0
        end = len(nums)-1
        while i <= end:
            if i == end:
                break
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                end -= 1
            else:
                i += 1
        return nums

    # Two Sum - Brute Force Way
    # Space Complexity = O(n)
    # Best Time Complexity = O(1)
    # Time Complexity = O(n^2)
    # Solved in 15 min
    def twoSumBrute(self, nums: list[int], target: int) -> list[int]:
        # A quick way to decide if we can just return [0,1]
        if len(nums) == 2 and nums[0] + nums[1] == target:
            return [0,1]
        # Below actually runs the basic algorithm
        indexes = []
        i = 0
        while i < len(nums) and len(indexes) < 2:
            j = i+1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    indexes.append(i)
                    indexes.append(j)
                j += 1
            i += 1
        return indexes
    
    # Two Sum - Hashmap
    # Best Space Complexity = O(n)
    # Space Complexity = O(n^2)
    # Best Time Complexity = O(1)
    # Time Complexity = O(n+k)
    # Solved in 30 min
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 2 and nums[0] + nums[1] == target:
            return [0,1]
        search = {}
        i = 0
        while i < len(nums):
            index = str(nums[i])
            if index in search:
                search[index].append(i)
            else:
                search[index] = [i]
            i += 1
        for key, val in search.items():
            diff = str(target - int(key))
            if diff == key and len(val) == 2:
                return val
            elif diff == key and len(val) > 2:
                return [val[0],val[1]]
            elif diff == key and len(val) < 2:
                continue
            elif diff in search:
                indexes = []
                indexes.append(val[0])
                indexes.append(search[diff][0])
                return indexes
