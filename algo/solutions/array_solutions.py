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

    # Do not return anything, modify nums1 in-place instead.
    # Space solution = O(1)
    # Best Time solution = O(1)
    # Average Time solution = O(n)
    # Solved in over 1 hour - Need to practice
    # def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
        # Don't add the else and if conditions for final leetcode solution
        if len(nums1) <= 0 and len(nums2) <= 0:
            return []
        elif len(nums1) <= 0:
            return nums2
        elif len(nums2) <= 0:
            return nums1
        i = 0
        while i < len(nums1) and len(nums2) > 0:
            # m is to help decide if the 0 is a placer or not
            if nums1[i] > nums2[0] and i < m:
                # Add in the initial position of nums2 at i in nums1
                nums1.insert(i, nums2.pop(0))
                # Remove the ending at nums1, increment m, decrement n
                nums1.pop()
                m+=1
                n-=1
            elif i >= m:
                # adding in the remaining in nums2 to nums1
                nums1.insert(i, nums2.pop(0))
                nums1.pop()
            i += 1
        return nums1
