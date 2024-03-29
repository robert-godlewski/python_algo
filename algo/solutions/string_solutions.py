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
