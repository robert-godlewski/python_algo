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

    # Minimum Index Sum of Two Lists
    # Best Time Complexity = O(1)
    # Time Complexity = O(n)
    # Best Space Complexity = O(1)
    # Space Complexity = O(n**2)
    # Solved in 40 min
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        if list1 == list2:
            return[list1[0]]
        common = {}
        # Adding in everything form list1 to common
        i = 0
        while i < len(list1):
            if list1[i] not in common:
                common[list1[i]] = {
                    'index_sum': i,
                    # 'in_list1': True, This is obvious
                    'in_list2': False
                }
            # else: whe skip this because we want the lowest index point
            i += 1
        # Now only checking and adding in values from list2 if they are in common but only taking the first possible index to add to the sum.
        j = 0
        while j < len(list2):
            if list2[j] in common and common[list2[j]]['in_list2'] is False:
                common[list2[j]]['in_list2'] = True
                common[list2[j]]['index_sum'] += j
            # else: if it's not in list1 then it's not a common phrase
            j += 1
        # Checking which sums from the list of common words.
        min_num = -1
        min_list = []
        for key in common.keys():
            if common[key]['in_list2'] is True:
                if min_num == -1:
                    min_list.append(key)
                    min_num = common[key]['index_sum']
                elif common[key]['index_sum'] < min_num:
                    min_list = [key]
                    min_num = common[key]['index_sum']
                elif common[key]['index_sum'] == min_num:
                    min_list.append(key)
        return min_list

    # First Unique Character in a String
    # Best Time Complexity = O(1)
    # Time Complexity = O(n)
    # Best Space Complexity = O(1)
    # Space Complexity = O(n**2)
    # Solved in 20 min
    def firstUniqChar(self, s: str) -> int:
        if len(s) < 1: 
            return -1
        elif len(s) == 1:
            return 0
        s_arr = list(s)
        char_position = {}
        i = 0
        while i < len(s):
            if s_arr[i] in char_position:
                char_position[s_arr[i]].append(i)
            else:
                char_position[s_arr[i]] = [i]
            i += 1
        first = -1
        for char in char_position.keys():
            if len(char_position[char]) == 1:
                if first == -1 or char_position[char][0] < first:
                    first = char_position[char][0]
        return first

    # Intersection of Two Arrays II - Need to study, not really a hashmap problem
    # Time Complexity = O(n), without sorting
    # Space Complexity = O(n), not including the sorting
    # Solved in over 30 min
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Step 1: sort both nums1 and nums 2
        # Might be best to maybe build a counting sort algorithm or bubble sort depending on circumstance
        nums1.sort()
        nums2.sort()
        # Step 2: go through both and add in every time they match
        answer = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                answer.append(nums1[i])
                i += 1
                j += 1
        return answer

    # Contains Duplicate II - Need to practice
    # Time Complexity = O(n)
    # Space Complexity = O(n**2)
    # Solved in 40 min
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        indexes = {}
        i = 0
        while i < len(nums):
            key = str(nums[i])
            if key in indexes:
                if i-indexes[key][len(indexes[key])-1] <= k:
                    return True
                indexes[key].append(i)
            else:
                indexes[key] = [i]
            i += 1
        return False
