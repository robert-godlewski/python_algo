# List of Solutions solved in Apr 2024
class Solution:
    # Binary Search - Brute Force
    # Time Complexity = O(n)
    # Space Complexity = O(1)
    # Solved in 5 min
    def searchBrute(self, nums: list[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            else:
                i += 1
        return -1

    # Binary Search - Optimized
    # Best Time Complexity = O(1)
    # Average Time Complexity = O(logn)
    # Space Complexity = O(1)
    # Solved in 30 min - Need to practice
    def bsearch(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
        return -1

    # Sqrt(x)
    # Time Complexity = O(1)
    # Space Complexity = O(1)
    # Solved in 1 min
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)

    # Search in Rotated Sorted Array - Taking too much time
    # Time Complexity
    # Space Complexity
    # 12:48
    # Still wrong
    '''
    Group 1 - Works
    _var_________|_val
    nums         | [4,5,6,7,0,1,2]
    target       | 0
    pivot        | -1 -> 4
    nums[pivot]  | null -> 0
    left         | 0
    nums[left]   | 4
    right        | 6
    nums[right]  | 2
    mid          | (0+6)//2=6//2=3
    nums[mid]    | 7

    Group 2 - Works
    _var_________|_val
    nums         | [4,5,6,7,0,1,2]
    target       | 5
    pivot        | -1->4
    nums[pivot]  | null->0
    left         | 0|
    nums[left]   | 4|
    right        | 6->3|
    nums[right]  | 2->7|
    mid          | (0+6)//2=6//2=3|(0+3)//2=3//2=1
    nums[mid]    | 7|5

    Group 3
    _var_________|_val
    nums         | [4,5,6,7,8,1,2,3]
    target       | 8
    pivot        | -1|->5
    nums[pivot]  | null|->1
    left         | 0->4|
    nums[left]   | 4->8|
    right        | 7|
    nums[right]  | 3|
    mid          | (0+7)//2=7//2=3|(4+7)//2=11/2=5
    nums[mid]    | 7|1
    '''
    def rsearch(self, nums: list[int], target: int) -> int:
        if len(nums) == 0: # False
            return -1
        # Need a way to find the index where the pivot point should be
        pivot = -1
        left = 0
        right = len(nums)-1
        while left <= right: # True|True
            mid = (left+right)//2
            if nums[mid] == target: # False|False
                return mid
            else:
                # nums[mid] != target: # True|True
                if nums[left] < nums[right]: # False|False
                    # we can do a normal binary search
                    if nums[mid] < target: # skip
                        left = mid+1
                    else: # nums[mid] > target: # skip
                        right = mid-1
                else: # nums[left] > nums[right]: # True|True
                    # Check the pivot index
                    if pivot == -1: # True
                        if nums[mid] < nums[mid-1]: # False|True
                            pivot = mid
                        elif nums[mid] > nums[mid+1]: # False|Skip
                            pivot = mid+1
                        # else: Still need to find the pivot from mid
                    if pivot != -1 and nums[pivot] == target: # False|False
                        return pivot
                    if nums[left] == target: # False
                        return left
                    if nums[right] == target: # False
                        return right
                    elif pivot != -1: # False|True
                        if nums[pivot] < target and nums[right] > target: # Skip|False
                            left = pivot
                        elif nums[left] < target and nums[pivot-1] > target: # Skip|False
                            right = pivot-1
                        elif nums[left] == target:
                            return left
                        elif nums[right] == target:
                            return right
                    else: # True
                        if nums[mid] < target and nums[left] < target: # True
                            left = mid+1
                        elif nums[mid] > target and nums[right] > target: # Skip
                            right = mid-1
                        elif nums[mid] < target and nums[right] < target: # Skip
                            right -= 1
                        elif nums[left] > target and nums[left] > target: # skip
                            left += 1
        # Haven't found the target at all
        return -1

    # Find Peak Element
    # Best Time Complexity = O(1)
    # Average Time Complexity = O(n)
    # Space Complexity = O(1)
    # Solved in 2 min
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        maxId = 0
        i = 1
        while i < len(nums):
            if nums[i] > nums[maxId]:
                maxId = i
            i += 1
        return maxId

    # Find Minimum in Rotated Sorted Array
    # Best Time Complexity = O(1)
    # Average Time Complexity = O(logn)
    # Space Complexity = O(1)
    # Solved in 30 min
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)-1
        minnum = 5000
        while left < right:
            mid = (left+right)//2
            if nums[mid] < minnum:
                minnum = nums[mid]
            if nums[left] < minnum:
                minnum = nums[left]
            else:
                left += 1
            if nums[right] < minnum:
                minnum = nums[right]
            else:
                right -= 1
        if left == right and nums[left] < minnum:
            minnum = nums[left]
        return minnum

    # Search for a Range - Bad solution
    # Best Time Complexity = O(1)
    # Time Complexity = 
    # Space Complexity =
    # Solved in 3:30
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1,-1]
        elif len(nums) == 1 and nums[0] == target:
            return [0,0]
        tar_range = [-1,-1]
        left = 0
        right = len(nums)-1
        while left + 1 < right:
            mid = (left+right)//2
            if nums[mid] == target:
                if tar_range[0] == -1 or mid < tar_range[0]:
                    tar_range[0] = mid
                if tar_range[1] == -1 or mid > tar_range[0]:
                    tar_range[1] = mid
                if nums[left] == target:
                    tar_range[0] = left
                    left = mid
                else:
                    left += 1
            elif nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
        if nums[left] == target and (left < tar_range[0] or tar_range[0] == -1):
            tar_range[0] = left
            if tar_range[1] == -1:
                tar_range[1] = left
        if nums[right] == target and right < len(nums) and right > tar_range[1]:
            tar_range[1] = right
            if tar_range[0] == -1:
                tar_range[0] = right
        return tar_range
