# Aug and Sep 2022 solutions
# My solution on Aug 2022 - had help from a youtube video
class MyHashSet:
    def __init__(self, length=10**6):
        # length is the maximum lenght of the set
        # maximum number of operations - needed for leetcode specific solution
        #self.max_opps = 10**4
        # creates a list full of empty values - Brute force way
        #self.hash_list = [None for i in range(self.set_length)]
        self.length = length
        self.hash_list = [[] for i in range(self.length)]

    def add(self, key):
        # Brute force way
        #if not self.contains(key): self.hash_list[key] = True
        subkey = key % self.length
        if not self.contains(key): self.hash_list[subkey].append(key)

    def remove(self, key):
        # Brute force way
        #if self.contains(key): self.hash_list[key] = None
        subkey = key % self.length
        if self.contains(key): self.hash_list[subkey].remove(key)

    def contains(self, key): 
        # Brute force way
        #return self.hash_list[key]
        subkey = key % self.length
        return key in self.hash_list[subkey]


# Brute Force Way and numbers are positive only
class HashSetBrute:
    def __init__(self, length=10**6) -> None:
        self.length = length
        self.hash_list = [0 for num in range(self.length)]

    def add(self, key: int, value: int) -> None:
        if not self.contains(key): self.hash_list[key] = value

    def remove(self, key: int) -> None:
        if self.contains(key): self.hash_list[key] = 0

    def contains(self, key: int) -> bool: 
        return self.hash_list[key]


# Used as a counter for a list of integers
class HashSetCounter:
    def __init__(self, length=10**6) -> None:
        self.length = length
        self.hash_list = [0 for i in range(self.length)]

    def add(self, key: int) -> None:
        if not self.contains(key): self.hash_list[key] = 1
        else: self.hash_list[key] += 1

    def contains(self, key: int) -> bool:
        return self.hash_list[key]


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
