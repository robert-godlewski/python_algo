class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_num = 0
        current_num = 0
        for i in nums:
            if i == 1: current_num += 1
            elif i == 0: current_num = 0
            if max_num < current_num: max_num = current_num
        return max_num
