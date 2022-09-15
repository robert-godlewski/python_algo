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

    # Solution in 30 min
    # nums1 and nums2 are both a list of int
    # returns a list of int
    def intersection(self, nums1: list, nums2: list) -> list:
        count_set = HashSetCounter(1000)
        '''
        i = 0
        while i < len(nums1):
            if count_set.hash_list[nums1[i]] == 0:
                count_set.add(nums1[i])
            i += 1
        i = 0
        while i < len(nums2):
            if count_set.hash_list[nums2[i]] == 1:
                count_set.add(nums2[i])
            i += 1
        '''
        self.counter(nums1, 0, count_set)
        self.counter(nums2, 1, count_set)
        result = []
        for k in range(1000):
            if count_set.hash_list[k] == 2:
                result.append(k)
        return result

    # Used for intersection
    def counter(self, nums: list, target: int, counts: HashSetCounter) -> None:
        i = 0
        while i < len(nums):
            if counts.hash_list[nums[i]] == target:
                counts.add(nums[i])
            i += 1
