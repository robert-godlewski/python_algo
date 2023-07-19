# A group of Binary Search Templates from leetcode
class BinarySearchTemps:
    def binarySearch1(nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        #left, right = 0, len(nums) - 1
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # End Condition: left > right
        return -1