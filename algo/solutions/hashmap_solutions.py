# Solved in August 2024
class Solution:
    # Leetcode Two Sum solution
    # Best Time Complexity = O(1)
    # Time Complexity = O(n**2)
    # Space Complexity = O(1)
    # Solved in 15 min
    def twoSumBrute(self, nums: list[int], target: int) -> list[int]: 
        i = 0
        while i < len(nums):
            j = i+1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i,j]
                j += 1
            i += 1
        return [0,1]

    # Best Time Complexity = O(1)
    # Time Complexity = O(n)
    # Best Space Complexity = O(1)
    # Space Complexity = O(n)
    # Solved in 20 min
    def twoSum(self, nums: list[int], target: int) -> list[int]: 
        if len(nums) == 2 and nums[0]+nums[1] == target:
            return [0,1]
        search = {}
        i = 0
        while i < len(nums):
            key = str(nums[i])
            if key in search:
                search[key].append(i)
            else:
                search[key] = [i]
            i += 1
        for key in search.keys():
            key_int = int(key)
            diff = str(target-key_int)
            if diff in search:
                if key != diff:
                    return [search[key][0],search[diff][0]]
                elif len(search[key]) >= 2:
                    return [search[key][0],search[key][1]]
        return [0,1]

    # Isomorphic Strings
    # Best Time Complexity = O(1)
    # Time Complexity = O(n)
    # Best Space Complexity = O(1)
    # Space Complexity = O(n)
    # Solved in 30 min
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if s == t:
            return True
        s_indexes = {}
        s_arr = list(s)
        t_indexes = {}
        t_arr = list(t)
        i = 0
        while i < len(s):
            if s_arr[i] in s_indexes and t_arr[i] in t_indexes:
                s_indexes[s_arr[i]].append(i)
                t_indexes[t_arr[i]].append(i)
            elif s_arr[i] not in s_indexes and t_arr[i] not in t_indexes:
                s_indexes[s_arr[i]] = [i]
                t_indexes[t_arr[i]] = [i]
            else:
                # Obviously s and t are not isomorphic
                return False
            i += 1
        i -= 1
        while i >= 0:
            if s_indexes[s_arr[i]] != t_indexes[t_arr[i]]:
                return False
            i -= 1
        # They are the same
        return True
