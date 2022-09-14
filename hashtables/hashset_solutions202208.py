# Aug and Sep 2022 solutions
from myhashset import MyHashSet, HashSetCounter


class Solution:
    # Actually using a hashset, solved in Aug
    # solved in 10 min
    def containsDuplicate(self, nums: list) -> bool:
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

    # Solution in 30 min, first one in Sep 2022
    # Had to design a new hashset that uses a counter like system instead
    def singleNumber(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            power = 10**4
            hashset = HashSetCounter(3*power)
            i = 0
            while i < len(nums):
                hashset.add(nums[i])
                i += 1
            num = None
            i = 0
            while i < len(nums):
                if hashset.hash_list[nums[i]] == 1:
                    num = nums[i]
                    break
                i += 1
            return num
