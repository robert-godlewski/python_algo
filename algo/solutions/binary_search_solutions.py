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

    # Search in Rotated Sorted Array
    # Time Complexity
    # Space Complexity
    # Still wrong
    '''
    _var_________|_val
    nums         | [4,5,6,7,0,1,2]
    target       | 5
    left         | 0
    nums[left]   | 4
    minInd       | 0 -> 6 -> 0|
    nums[minInd] | 4 -> 2 -> 4|
    right        | 6 -> 2|
    nums[right]  | 2 -> 6|
    maxInd       | 6 -> 0 -> 2|
    nums[maxInd] | 2 -> 4 -> 6|
    mid          | (0+6)//2=>6//2=>3|(0+2)//2=>2//2=>1
    nums[mid]    | 7|5
    temp         | 0|
    '''
    def rsearch(self, nums: list[int], target: int) -> int:
        if len(nums) == 0: # False
            return -1
        # minInd and maxInd keeps track of the placement of the minimum and maximum indexes
        left = 0
        minInd = 0
        right = len(nums)-1
        maxInd = len(nums)-1
        while left <= right: # True|True
            mid = (left+right)//2
            # adjusting the placement of the min and max indexes based on search
            if nums[minInd] > nums[maxInd]: # True|False
                temp = minInd
                minInd = maxInd
                maxInd = temp
            if nums[mid] == target: # False|True
                return mid
            elif nums[minInd] == target: # False
                return minInd
            elif nums[maxInd] == target: # False
                return maxInd
            elif nums[mid] < target and minInd == left: # False
                left = mid+1
                minInd = mid+1
            elif nums[mid] > target and maxInd == right: # False
                right = mid-1
                maxInd = mid-1
            else: # True
                # We have switched the minInd and maxInd
                if nums[mid] < target: # False
                    # Fix this?
                    if nums[right] > target and nums[left] > target: # Skip
                        # Go right
                        left = mid+1
                        minInd = mid+1
                        maxInd = right
                    else: # Skip
                        # Go left
                        right = mid-1
                        maxInd = mid-1
                        minInd = left
                else: # True
                    # nums[mid] > target:
                    if nums[right] < target and nums[left] < target: # True
                        # Go left
                        right = mid-1
                        maxInd = mid-1
                        minInd = left
                    else: # False
                        # nums[right] > target and nums[left] > target: 
                        # Go right
                        left = mid+1
                        minInd = mid+1
                        maxInd = right
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
