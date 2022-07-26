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
    
    # Do not return anything, modify nums1 in-place instead. - Usual O(n), Best O(1) solution - Bad solution, This is a merge sort algorithm on an array
    # solved in 20 min
    def merge(self, nums1, m, nums2, n):
        length = m+n
        i = 0
        j = 0
        while i < length:
            print(f"nums1 = {nums1}")
            print(f"m = {m}")
            print(f"nums2 = {nums2}")
            print(f"n = {n}")
            print(f"i = {i}")
            print(f"j = {j}")
            if len(nums2) == 0:
                break
            if nums1[i] == 0 or nums1[i] > nums2[j]:
                if nums1[i] == 0:
                    nums1[i] = nums2[j]
                    j += 1
                else:
                    temp = nums1[i]
                    nums1[i] = nums2[j]
                    nums2[j] = temp
            i += 1
        # Need to learn Merge sort algorithm
        # Don't add this to leetcode
        return nums1
