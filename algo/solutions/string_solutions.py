# String Solutions Mar 2024
# Got the Easy Collection from the Top Interview Questions group
class Solution:
    def __init__(self) -> None: pass

    # Reverse String
    # Space Complexity = O(1)
    # Time Complexity = O(n)
    # Solved in 5 min
    # To submit in leetcode: Do not return anything, modify s in-place instead.
    # def reverseString(self, s: list[str]) -> None:
    def reverseString(self, s: list[str]) -> list[str]:
        i = 0
        while i < len(s)//2:
            temp = s[len(s)-1-i]
            s[len(s)-1-i] = s[i]
            s[i] = temp
            i += 1
        return s

    # Reverse Integer
    # Space Complexity = O(n)
    # Time Complexity = O(n)
    # Solved in 20 min
    # The method in leetcode was called reverse but we are changing it to reverseInt
    def reverseInt(self, x: int) -> int:
        x_str = str(x)
        x_arr = list(x_str)
        x_neg = ""
        if x_arr[0] == "-":
            x_neg = x_arr.pop(0)
        i = 0
        while i < len(x_arr)//2:
            temp = x_arr[i]
            x_arr[i] = x_arr[len(x_arr)-1-i]
            x_arr[len(x_arr)-1-i] = temp
            i += 1
        new_str = ""
        if x_neg == "-":
            new_str = "-"
        for num in x_arr:
            new_str += num
        new_int = int(new_str)
        # Need the if-else here due to leetcode's special requirements
        if new_int <= -2**31 or new_int > 2**31:
            return 0
        else:
            return new_int

    # First Unique Character in a String
    # Space Complexity = O(1)
    # Best Time Complexity = O(1)
    # Average Time Complexity = O(nlogn)
    # Solved in 20 min
    def firstUniqChar(self, s: str) -> int:
        if len(s) < 1:
            return -1
        elif len(s) == 1:
            return 0
        else:
            ans = 0
            i = 0
            while i < len(s):
                if ans >= len(s):
                    return -1
                if ans == i:
                    pass
                elif s[ans] == s[i]:
                    ans += 1
                    i = -1
                i += 1
            return ans

    # Valid Anagram
    # Best Space Complexity = O(1)
    # Average Space Complexity = O(n)
    # Best Time Complexity = O(1)
    # Average Time Complexity = O(n)
    # Solved in 15 min
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def wordHash(word: str) -> dict:
            hash = {}
            i = 0
            while i < len(word):
                if word[i] not in hash:
                    hash[word[i]] = 1
                else:
                    hash[word[i]] += 1
                i += 1
            return hash
        s_hash = wordHash(s)
        t_hash = wordHash(t)
        for key in s_hash.keys():
            if key not in t_hash:
                return False
            if s_hash[key] != t_hash[key]:
                return False
        return True
