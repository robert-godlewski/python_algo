# Aug and Sep 2022 solutions
from myhashset import MyHashSet, HashSetCounter, HashSetBrute


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

    def isHappy(self, n: int, sum_set=None) -> bool:
        # returns true if the looping process ends with 1
        print(f"n in: {n}")
        n_str = str(n)
        # Base cases to end the loop
        if len(n_str) == 1 and n**2 == 1:
            return True
        if not sum_set:
            # Builds the Hash Set if not already built
            two_pow = 2**10
            #two_pow = 2**31
            sum_set = MyHashSet(two_pow-1)
            print("created hashset")
        n_list = list(n_str)
        print(f"n digit split: {n_list}")
        square_sum = 0
        for num_str in n_list:
            num = int(num_str)
            square_sum += num**2
        # another base case to exit a for loop or recurse
        if sum_set.contains(square_sum):
            return False
        else:
            sum_set.add(square_sum)
            return self.isHappy(square_sum, sum_set)
