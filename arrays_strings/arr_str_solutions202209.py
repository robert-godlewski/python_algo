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
    '''
    __var__|_val
    mat    | [[1,2,3],[4,5,6],[7,8,9]]
    m      | 3
    n      | 3
    nums   | []
    row    | 0
    col    | 0
    i      | 0
    '''
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []
        print(f"matrix in = {mat}")
        m = len(mat)
        print(f"m = {m}")
        n = len(mat[0])
        print(f"n = {n}")
        nums = []
        row = 0
        col = 0
        i = 0
        while i < m * n:
            print(f"nums = {nums}")
            print(f"row = {row}")
            print(f"col = {col}")
            nums.append(mat[row][col])
            #
            i += 1
        # For example
        '''
        nums.append(mat[0][0])
        #
        nums.append(mat[0][1])
        nums.append(mat[1][0])
        #
        nums.append(mat[2][0])
        nums.append(mat[1][1])
        nums.append(mat[0][2])
        #
        nums.append(mat[1][2])
        nums.append(mat[2][1])
        #
        nums.append(mat[2][2])
        '''
        return nums

    # matrix is a nested list of int
    # returns a list of int
    # Solved in - Took a while to solve, works in most cases
    def spiralOrder(self, matrix):
        print(f"matrix in = {matrix}")
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        print(f"matrix is a {m} X {n} grid")
        nums = []
        row = 0
        col = 0
        # the index of the boundary
        bound = 0
        is_x = True
        forwards = True
        i = 0
        while i < m * n:
            print(f"matrix[{row}][{col}] = {matrix[row][col]}")
            nums.append(matrix[row][col])
            if n == 1:
                row += 1
            else:
                if is_x and forwards:
                    col += 1
                    if col == n-1-bound:
                        is_x = False
                elif not is_x and forwards and row+1 < m:
                    row += 1
                    if row == m-1-bound:
                        forwards = False
                        is_x = True
                elif is_x and not forwards:
                    col -= 1
                    if col == bound:
                        is_x = False
                elif not is_x and not forwards and row >= 0:
                    row -= 1
                    if row == bound+1:
                        bound += 1
                        forwards = True
                        is_x = True
            i += 1
        return nums

    # Based off of Pascal's triangle
    # numRows = the number of rows in the array
    # numRows is an int
    # returns nested list of int
    def generate(self, numRows):
        if numRows < 1 or numRows > 30:
            return []
        else:
            pascal = [[] for i in range(numRows)]
            print(pascal)
            i = 0
            while i < len(pascal):
                if i == 0:
                    pascal[i].append(1)
                else:
                    j = 0
                    while j <= i:
                        if j == 0 or j == i:
                            pascal[i].append(1)
                        else:
                            temp = pascal[i-1][j-1] + pascal[i-1][j]
                            pascal[i].append(temp)
                        j += 1
                print(pascal[i])
                i += 1
            return pascal
