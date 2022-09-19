# Solutions in Sep 2022
class Solution:
    # Solved in 15 min
    # O(n**2) time solution - Most cases
    # Best time solution = O(1)
    def twoSumBrute(self, nums: list, target: int) -> list:
        # nums is a list of int
        # returns a list of int
        # Base Case
        if len(nums) == 2:
            return [0,1]
        indexes = []
        i = 0
        while i < len(nums):
            j = i+1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    indexes.append(i)
                    indexes.append(j)
                    break
                j += 1
            if len(indexes) > 0:
                break
            i += 1
        return indexes

    # Solved in 45 min
    # O(n) time solution
    # Uses a dictionary for the values
    def twoSum(self, nums: list, target: int) -> list:
        # nums is a list of int
        # returns a list of int
        diff_map = {}
        i = 0
        while i < len(nums):
            #print(nums[i])
            key = target-nums[i]
            #print(key)
            if key not in diff_map:
                diff_map[key] = [i]
            else:
                diff_map[key].append(i)
            i += 1
        #print(diff_map)
        indexes = []
        for k in diff_map:
            if target % 2 == 0 and len(diff_map[k]) > 1:
                if nums[diff_map[k][0]] * 2 == target:
                    indexes.append(diff_map[k][0])
                    indexes.append(diff_map[k][1])
            diff = target-k
            if diff in diff_map and diff != k:
                indexes.append(diff_map[k][0])
                indexes.append(diff_map[diff][0])
            if len(indexes) > 0:
                break
        return indexes
