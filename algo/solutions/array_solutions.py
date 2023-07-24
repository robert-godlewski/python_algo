# Solutions in Jul 2023
class Solution:
    # Do not return anything, modify arr in-place instead.
    # Space solution = O(1)
    # Time solution = O(n)
    # Solved in 5 min
    #def duplicateZeros(self, arr: list[int]) -> None:
    def duplicateZeros(self, arr: list[int]) -> list[int]:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i,0)
                i += 1
                arr.pop()
            i += 1
        return arr
