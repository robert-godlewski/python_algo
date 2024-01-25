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
