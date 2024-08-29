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

    # Leetcode Isomorphic Strings Solution
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

    # Leetcode Minimum Index Sum of Two Lists Solution - Need to study
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

    # Leetcode First Unique Character in a String - Solution
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

    # Leetcode Intersection of Two Arrays II Solution - Need to study, not really a hashmap problem
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

    # Leetcode Contains Duplicate II Solution - Need to practice
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

    # Leetcode Group Anagrams Solution
    # Best Time Complexity = O(1)
    # Time Complexity = O(nlogn)
    # Best Space Complexity = O(1)
    # Space Complexity = O(n**2)
    # Solved actual problem in 30 min but built the letter sorter in 1 hr

    # Need this to sort the letters within a word from a-z to build keys
    # Time Complexity = O(nlogn)
    # Space Complexity = O(n**2)
    # Took 1 hr to build
    def _letterSort(self, word: str) -> str:
        letters = list(word)
        letter_position = {
            "a": {"index": 0, "count": 0},
            "b": {"index": 1, "count": 0},
            "c": {"index": 2, "count": 0},
            "d": {"index": 3, "count": 0},
            "e": {"index": 4, "count": 0},
            "f": {"index": 5, "count": 0},
            "g": {"index": 6, "count": 0},
            "h": {"index": 7, "count": 0},
            "i": {"index": 8, "count": 0},
            "j": {"index": 9, "count": 0},
            "k": {"index": 10, "count": 0},
            "l": {"index": 11, "count": 0},
            "m": {"index": 12, "count": 0},
            "n": {"index": 13, "count": 0},
            "o": {"index": 14, "count": 0},
            "p": {"index": 15, "count": 0},
            "q": {"index": 16, "count": 0},
            "r": {"index": 17, "count": 0},
            "s": {"index": 18, "count": 0},
            "t": {"index": 19, "count": 0},
            "u": {"index": 20, "count": 0},
            "v": {"index": 21, "count": 0},
            "w": {"index": 22, "count": 0},
            "x": {"index": 23, "count": 0},
            "y": {"index": 24, "count": 0},
            "z": {"index": 25, "count": 0}
        }
        for letter in letters:
            if letter in letter_position:
                letter_position[letter]["count"] += 1
        answer = ""
        for key in letter_position.keys():
            count = letter_position[key]["count"]
            while count > 0:
                answer += key
                count -= 1
        return answer

    # This is the actual solution for Leetcode Group Anagrams
    # Average Time Complexity without sorting = O(n)
    # Average Space Complexity without sorting = O(n)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) <= 1:
            return [strs]
        anagrams = {}
        for word in strs:
            key_word = self._letterSort(word)
            if key_word in anagrams:
                anagrams[key_word].append(word)
            else:
                anagrams[key_word] = [word]
        answer = []
        for value in anagrams.values():
            answer.append(value)
        return answer
