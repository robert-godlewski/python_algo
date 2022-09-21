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

    # Solved in 20 min but incorrect, I still don't really understand the problem
    # Best time = O(1)
    # Time = O(n)
    def isIsomorphicAttempt(self, s: str, t: str) -> bool:
        print(s)
        print(t)
        # Base cases
        if len(s) != len(t):
            return False
        elif s == t:
            return True
        s_list = list(s)
        print(s_list)
        t_list = list(t)
        print(t_list)
        s_dict = self.mapLetters(s_list)
        print(s_dict)
        t_dict = self.mapLetters(t_list)
        print(t_dict)
        s_counts = self.letcounts(s_dict)
        print(s_counts)
        t_counts = self.letcounts(t_dict)
        print(t_counts)
        if s_counts == t_counts:
            return True
        else:
            return False

    # used for isIsomorphic
    def mapLetters(self, letters: str) -> dict:
        letter_count = {}
        for letter in letters:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        return letter_count

    # used for isIsomorphic
    def letcounts(self, letters: dict) -> list:
        counts = []
        for k in letters:
            counts.append(letters[k])
        return counts

    # Leetcode solution
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_t = {}
        mapping_t_s = {}
        for c1, c2 in zip(s, t):
            # Case 1: No mapping exists in either of the dictionaries
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1
            # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both            
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False
        return True

    # Bad Solution - for some reason there is a bug but I don't know why
    def findRestaurant(self, list1: list, list2: list) -> list:
        # list1 and list2 are both a list of str
        # returns a list of str
        # Base case
        if list1 == list2:
            return [list1[0]]
        # Mapping the phrases with the indexes
        common_dict = {}
        i = 0
        while i < len(list1):
            if list1[i] not in common_dict:
                common_dict[list1[i]] = [i]
            else:
                common_dict[list1[i]].append(i)
            i += 1
        i = 0
        while i < len(list2):
            if list2[i] not in common_dict:
                common_dict[list2[i]] = [i]
            else:
                common_dict[list2[i]].append(i)
            i += 1
        print(common_dict)
        # Finding the min
        min_list = []
        min_val = None
        for key in common_dict:
            if len(common_dict[key]) == 2:
                subtotal = common_dict[key][0] + common_dict[key][1]
                if min_val is None:
                    min_val = subtotal
                    min_list.append(key)
                elif subtotal == min_val:
                    min_list.append(key)
                elif subtotal < min_val:
                    min_val = subtotal
                    min_list = [key]
            print(f"Current list = {min_list}")
            print(f"Current min sum = {min_val}")
        return min_list
