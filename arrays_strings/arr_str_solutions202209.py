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

    # Adding 1 in an array
    # digits = list of int
    # return a list of int
    # Solution - 20 min
    # Best case = O(1)
    # usual case = O(n)
    def plusOne(self, digits):
        print(f"list in = {digits}")
        digit = len(digits)-1
        if digits[digit] == 9:
            num_str = ""
            for i in digits:
                stri = str(i)
                num_str += stri
            num = int(num_str)
            num += 1
            num_str = str(num)
            digits = list(num_str)
            i = 0
            while i < len(digits):
                digits[i] = int(digits[i])
                i += 1
        else:
            digits[digit] += 1
        print(f"list out = {digits}")
        return digits

    # mat is a m*n matrix that's a list with a list of int
    # returns a list of int
    # Solution - Took me over 1 hr, still doesn't work
    def findDiagonalOrder(self, mat):
        #if not mat or not mat[0]:
        return []
        print(f"matrix in = {mat}")
        m = len(mat)
        print(f"m = {m}")
        n = len(mat[0])
        print(f"n = {n}")
        nums = []
        # determines if going down or up
        is_d = False
        row = 0
        col = 1
        while row < m and col < n:
            print(f"nums = {nums}")
            print(f"row = {row}")
            print(f"col = {col}")
            print(f"is going down? {is_d}")
            nums.append(mat[row][col])
            if is_d:
                row += 1
                if col != 0:
                    col -= 1
            else:
                if row != 0:
                    row -= 1
                col += 1
            if col != 0:
                is_d = True
            else:
                is_d = False
        return nums
