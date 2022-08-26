# Solutions in Aug 2022 -
class Solution:
    # find the index where everything to the left = the sum to the left of the index number
    # nums = list of int
    # Returns an int that corresponds to the index
    # Solved - Unsucessfully due to time limit exceeded error in leetcode but works with these condutions, O(nlog(n)) solution
    # recursive sum
    def arr_sum(self, nums, subtotal=0):
        if len(nums) == 1:
            return subtotal + nums[0]
        else:
            subtotal += nums.pop()
            return self.arr_sum(nums, subtotal)
        
    def pivotIndex(self, nums):
        print(f"nums in = {nums}")
        i = 0
        while i < len(nums):
            if len(nums) > 10**4:
                break
            print(i)
            # Left sum
            if i == 0:
                left = 0
            else:
                left = self.arr_sum(nums[:i])
            # right sum
            if i == len(nums) - 1:
                right = 0
            else:
                right = self.arr_sum(nums[i+1:])
            print(f"does {left} = {right}?")
            if left == right:
                print("yes")
                return i
            else:
                print("no")
            i += 1
        # if nothing is returned from before
        return -1

    # finding the biggest double in an array
    # nums = list of integers
    # Solution - Solved in 10 min, O(n) solution, Incorrect for some reason?
    def dominantIndex(self, nums):
        max_num = 0
        maxi = -1
        i = 0
        while i < len(nums):
            print(f"max num = {max_num}")
            print(f"max num index = {maxi}")
            if nums[i] > max_num:
                max_num = nums[i]
                maxi = i
            i += 1
        prev = maxi - 1
        compare = nums[prev] * 2
        if compare == 0:
            compare = max_num
        print(f"is {compare} = {max_num}")
        if compare == max_num:
            return maxi
        else:
            return -1
