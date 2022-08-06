# Aug 2022 solutions
from myhashset import MyHashSet


class Solution:
    # 15 min
    # O(n^2) solution - Works but crashes leetcode due to time limit exceeded
    '''
    def containsDuplicate(self, nums):
        # nums is a list of int
        i = 0
        while i < len(nums):
            compare = nums[i]
            j = i+1
            while j < len(nums):
                if nums[j] == compare: return True
                else: j += 1
            i += 1
        return False
    '''

    # Actually using a hashset
    # solved in 10 min
    def containsDuplicate(self, nums):
        # nums is a list of int
        # checks to see if there are duplicates
        dup = False
        hashset = MyHashSet(10**5)
        for i in nums:
            if hashset.contains(i):
                dup = True
                break
            hashset.add(i)
        return dup
