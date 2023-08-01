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

    # Space solution = O(1)
    # Time Solution = O(n)
    # Solved in 5 min
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                nums.append('_')
            elif nums[i] == '_':
                break
            else:
                i += 1
        print(f"nums = {nums}")
        return i

    # Space solution = O(1)
    # Time solution = O(n)
    # Solved in 20 min
    def removeDuplicates(self, nums: list[int]) -> int:
        # the number of unique values
        k = 0
        i = 0
        while i < len(nums):
            if i == 0:
                i += 1
            elif i > 0 and nums[k] == nums[i]:
                nums.pop(i)
                #nums.append('_')
            elif i > 0 and nums[k] != nums[i]: # and nums[i] != '_':
                k += 1
                i += 1
            # elif nums[i] == '_': break
        # increment because k was represented at an index value
        if len(nums) > 0: 
            k += 1
        print(f"nums = {nums}")
        return k

    # Space solution = O(1)
    # Best time solution = O(1)
    # Average Time solution = O(n)
    # Solved in 16 minutes
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) <= 1:
            return False
        is_going_up = True
        is_going_down = False
        i = 1
        while i < len(arr):
            if arr[i-1] == arr[i] and i-1 >= 0:
                return False
            elif is_going_up and arr[i-1] > arr[i] and i-1 == 0:
                return False
            elif is_going_down and arr[i-1] < arr[i] and i-1 >= 0:
                return False
            elif is_going_up and arr[i-1] > arr[i] and i-1 >= 0:
                is_going_down = True
                is_going_up = False
                i += 1
            else:
                i += 1
        if is_going_up and not is_going_down:
            return False
        else:
            return True
