# Solutions solved  in July 2022
class Solution:
    # Do not return anything, modify arr in-place instead.
    # Solved under 30 min
    def duplicateZeros(self, arr):
        #print(f"arr in = [{arr}]")
        i = 0
        while i < len(arr): # true
            #print(f"arr = [{arr}]")
            #print(f"i = {i}")
            #print(f"arr[i] = {arr[i]}")
            if arr[i] == 0: # true
                arr.insert(i, 0)
                arr.pop()
                i += 1
            i += 1
        # Don't add this to leet code
        return arr
