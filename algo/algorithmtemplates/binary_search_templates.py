# Got the base of these templates from LeetCode
class BS:
    # These are Binary Search Templates
    def __init__(self) -> None: pass

    def runTests(self) -> None:
        # This will run all of the tests for most of the binary search algorithms
        pass

    def temp1(self, nums: list[int], target: int) -> int:
        # This is the most basic binary search algorithm possible
        # Ideally nums is a sorted array in ascending order
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                # nums[mid] > target:
                right = mid-1
        # Still haven't found the target
        return -1

    def temp2(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        # left == right
        if nums[left] == target:
            return left
        return -1

    def temp3(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)-1
        while left + 1 < right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
        # left + 1 == right
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
