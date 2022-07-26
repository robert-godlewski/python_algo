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
    
    # Do not return anything, modify nums1 in-place instead. - Usual O(n), Best O(1) solution
    # solved in an hour - need to practice
    def merge(self, nums1, m, nums2, n):
        #print(f"nums1 = {nums1}")
        #print(f"m = {m}")
        #print(f"nums2 = {nums2}")
        #print(f"n = {n}")
        # combining both arrays
        #print("Combining nums1 and nums2")
        length = m+n
        i = m
        j = 0
        while i < length:
            #print(f"nums1[{i}] = {nums1[i]}")
            #print(f"nums2[{j}] = {nums2[j]}")
            nums1[i] = nums2[j]
            i += 1
            j += 1
        #print(f"nums1 = {nums1}")
        # sorting nums1
        #print("sorting nums1")
        nums1 = self.mergeSort(nums1)
        #print(f"returning {nums1}")
        # Don't add this to leetcode
        return nums1
    
    # part of merge algorithm - found most on Geeks for Geeks online
    def mergeSort(self, arr):
        #print(f"arr in = {arr}")
        if len(arr) > 1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            left = self.mergeSort(left)
            right = self.mergeSort(right)
            i = 0
            j = 0
            k = 0
            # sorting the 2 together
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            # adding in all of the remaining left side
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            # adding in all of the remaining right side
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        return arr
