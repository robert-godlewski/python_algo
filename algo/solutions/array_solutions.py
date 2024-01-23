# Array Solutions Jan 2024
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
    # Need to solve on LeetCode
    def maxProfit(self, prices: list[int]) -> int: return 0
