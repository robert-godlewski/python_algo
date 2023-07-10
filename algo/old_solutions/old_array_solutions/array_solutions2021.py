class Solution:
    # nums should be a list with all of these solutions

    # Finds the maximum times that the list nums has a 1 in order.
    def findMaxConsecutiveOnes(self, nums):
        max_num = 0
        current_num = 0
        for i in nums:
            if i == 1: current_num += 1
            elif i == 0: current_num = 0
            if max_num < current_num: max_num = current_num
        return max_num

    # Finds out and returns the number of numbers in nums that have an
    # even amount of digits.
    def findNumbers(self, nums): 
        even_digit_nums = 0
        for i in nums:
            if len(str(i)) % 2 == 0: even_digit_nums += 1
        return even_digit_nums

    # O(n**2) solution - need to find a better one
    def sortedSquaresNestedLoop(self, nums):
        print(f"Original list is: {nums}")
        i = 0
        while i <len(nums):
            print(f"index of nums we are on: {i}")
            print(f"currently squaring {nums[i]}")
            if nums[i] != 0:
                squ = nums[i]**2
                nums[i] = squ
            print(f"the squared number is {nums[i]}")
            i += 1
        print(f"Unordered list is: {nums}")
        for index in range(1, len(nums)):
            value = nums[index]
            i = index-1
            while i >= 0:
                if value < nums[i]:
                    nums[i+1] = nums[i]
                    nums[i] = value
                    i -= 1
                else: break
        print(f"Ordered list is: {nums}")
        return nums

    # Recursive O(N) solution - Leetcode times out for some reason still
    def sortedSquares(self, nums):
        # print(f"current list working on is: {nums}")
        if nums is None: return list()
        num = nums.pop()
        # print(f"the current number working on is: {num}")
        if num != 0: num = num**2
        # print(f"num squared is: {num}")
        if len(nums) > 0: nums = self.sortedSquares(nums)
        elif len(nums) == 0:
            nums.append(num)
            # print(f"first of the ordered list: {nums}")
            return nums
        i = 0
        # print("-----Entering the sorting phase---------")
        while i < len(nums):
            # print(f"nums[i] is: {nums[i]}")
            if nums[i] > num:
                nums.insert(i, num)
                break
            elif i == len(nums)-1:
                nums.append(num)
                break
            i += 1
        # print(f"List is now: {nums}")
        return nums

    def duplicateZeros(self, arr):
        i = 0
        # print(len(arr))
        while i < len(arr):
            # print(f'Index: {i}')
            # print(f'Value: {arr[i]}')
            if arr[i] == 0: 
                arr.insert(i, 0)
                arr.pop()
                i += 1
            i += 1

    # Solution that doesn't work
    def merge(self, nums1, m, nums2, n):
        max = m + n
        # print(f'Max = {max}')
        i = 0
        while i < max:
            if len(nums2) != 0:
                if nums1[i] >= nums2[0]:
                    nums1.insert(i, nums2[0])
                    nums1.pop()
                    nums2.pop(0)
            if nums1[i] == 0 and len(nums2) == 0:
                nums1.pop(i)
            i += 1
        # print(nums1)

    def removeElement(self, nums, val):
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                nums.append('_')
                k -= 1
            i += 1
            k += 1
        return k
