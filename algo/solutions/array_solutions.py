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

    # Space Solution = O(1)
    # Time Solution = O(n)
    # Solved in 8 min
    def replaceElements(self, arr: list[int]) -> list[int]:
        i = len(arr)-1
        maxVal = -1
        while i >= 0:
            temp = arr[i]
            arr[i] = maxVal
            if temp > maxVal:
                maxVal = temp
            i -= 1
        return arr
    
    # Do not return anything, modify nums in-place instead.
    # Space Solution = O(1)
    # Time Solution = O(n)
    # Solved in 5 min
    # def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        zeroIndex = len(nums)-1
        i = 0
        while i < zeroIndex:
            if i != zeroIndex and nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                zeroIndex -= 1
            else:
                i += 1
        # Don't return when submitting to leetcode
        return nums

    # Return array with even numbers in front and odd in the back
    # Space Solution = O(1)
    # Time Solution = O(n)
    # Solved in 10 min
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        i = 0
        end = len(nums)-1
        while i < end:
            if nums[i] % 2 != 0:
                temp = nums.pop(i)
                nums.append(temp)
                end -= 1
            else:
                i += 1
        return nums

    # Space solution
    # Time solution
    # Can't figure this out, Leetcode is too ambiguous
    def heightChecker(self, heights: list[int]) -> int:
        missmatchCount = 0
        expected = [heights[0]]
        i = 1
        while i < len(heights):
            expected.append(heights[i])
            # print(f"Heights = {heights}")
            # print(f"Expected = {expected}")
            # print(i)
            if heights[i-1] > heights[i]:
                missmatchCount += 1
                if i-1 >= 0:
                    expected[i-1] = heights[i]-1
            i += 1
        return missmatchCount

    # Space solution = O(1)
    # Time Solution = O(n**2)
    # Solved in 1 hr - need to work on quickening up the pace for this
    def pivotIndex(self, nums: list[int]) -> int:
        i = 0
        left_sum = 0
        right_sum = 0
        while i < len(nums):
            if len(nums) > 10**4:
                break
            if i == 0:
                # need to actually build out the right_sum initially
                j = 1
                while j < len(nums):
                    right_sum += nums[j]
                    j += 1
            else:
                # Update the sum values based off of new pivot
                right_sum -= nums[i]
                left_sum += nums[i-1]
            if left_sum == right_sum:
                return i
            i += 1
        return -1

    # Space solution = O(1)
    # Best Time solution = O(1)
    # Time solution = O(n)
    # Solved in 30 min
    def dominantIndex(self, nums: list[int]) -> int:
        maxIndex = 0
        secMaxIndex = 0
        if len(nums) < 2:
            return -1
        elif len(nums) >= 2:
            if nums[0] < nums[1]:
                maxIndex = 1
            elif nums[0] > nums[1]:
                secMaxIndex = 1
        i = 2
        while i < len(nums):
            if nums[i] > nums[maxIndex]:
                secMaxIndex = maxIndex
                maxIndex = i
            elif nums[i] < nums[maxIndex] and nums[i] > nums[secMaxIndex]:
                secMaxIndex = i
            i += 1
        if nums[secMaxIndex] * 2 <= nums[maxIndex]:
            return maxIndex
        else:
            return -1

    # Space solution = O(1)
    # Time solution = O(1)
    # Worst Time solution = O(n)
    # Solved in 15 min
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits)-1
        while i >= 0:
            if digits[i]+1 > 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                i -= 1
            else:
                digits[i] += 1
                break
        return digits

    # Space solution
    # Time solution
    # Bad solution
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m = 0
        n = 0
        ans = []
        # while m < len(mat) and n < len(mat[0]):
        #     print(f"m = {m}")
        #     print(f"n = {n}")
        #     print(f"matrix value = {mat[m][n]}")
        #     ans.append(mat[m][n])
        #     if m+1 == len(mat) and n+1 == len(mat):
        #         break
        #     if mat[m][n]%2 == 0:
        #         # going left and down
        #         m += 1
        #         if n > 0:
        #             n -= 1
        #     else:
        #         # going right and up
        #         if m > 0:
        #             m -= 1
        #         n += 1
        return ans

    # Space Solution = O(n)
    # Best time solution = O(1)
    # Time Solution = O(mn)
    # could not figure out within 1 hr - need to practice
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        row = 0
        col = 0
        # Use as a stopper when we have already added in a group of numbers
        bound = 0
        # Moving within the matrix subarray
        moving_in_row = True
        # Incrementing the index
        moving_positive = True
        i = 0
        while i < m*n:
            # print(f"matrix[{row}][{col}] = {matrix[row][col]}")
            # print(f"Moving in row? {moving_in_row}")
            # print(f"Moving in a positive direction? {moving_positive}")
            ans.append(matrix[row][col])
            if n == 1:
                # We just increment the rows because the length of each row list is 1
                row += 1
            else:
                if moving_in_row and moving_positive:
                    col += 1
                    if col == n-1-bound:
                        moving_in_row = False
                elif moving_positive and row+1 < m:
                    row += 1
                    if row == m-1-bound:
                        moving_in_row = True
                        moving_positive = False
                elif moving_in_row:
                    col -= 1
                    if col == bound:
                        moving_in_row = False
                elif not moving_in_row and not moving_positive and row >= 0:
                    row -= 1
                    if row == bound+1:
                        bound += 1
                        moving_in_row = True
                        moving_positive = True
            i += 1
        return ans

    # Space Solution = O(n**2)
    # Best time solution = O(1)
    # Time Solution = O(n**2)
    # Solved in 1 hr - Need to practice because we needed to check things
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows < 1 or numRows > 30:
            return []
        else:
            # Creating a nested empty array
            pascal = [[] for _ in range(numRows)]
            i = 0
            while i < len(pascal):
                if i == 0:
                    pascal[i].append(1)
                else:
                    j = 0
                    while j <= i:
                        if j == 0 or j == 1:
                            pascal[i].append(1)
                        else:
                            # look at the last list and the 2 before
                            temp = pascal[i-1][j-2] + pascal[i-1][j-1]
                            # insert it just before the current ending
                            pascal[i].insert(j-1, temp)
                        j += 1
                i += 1
            return pascal

    # Space Solution = O(n)
    # Best Time Solution = O(1)
    # Time Solution = O(n)
    # Solved in 45 min
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < 1 or len(a) > 10**4 or len(b) < 1 or len(b) > 10**4:
            return "0"
        # Making it so that the lengths of the 2 binary numbers are equal length
        a_arr = list(a)
        b_arr = list(b)
        if len(a_arr) < len(b_arr):
            i = len(a_arr)
            while i < len(b):
                a_arr.insert(0,"0")
                i += 1
        elif len(a_arr) > len(b_arr):
            i = len(b_arr)
            while i < len(a):
                b_arr.insert(0,"0")
                i += 1
        # Creating the sum result in ans and keeping track if there is any carry over 1s
        ans = ""
        carry_over = False
        i = len(a_arr)-1
        while i >= 0:
            if carry_over:
                if a_arr[i] == "0" and b_arr[i] == "0":
                    ans = "1"+ans
                    carry_over = False
                elif a_arr[i] == "1" and b_arr[i] == "1":
                    ans = "1"+ans
                else:
                    ans = "0"+ans
            else:
                if a_arr[i] == "0" and b_arr[i] == "0":
                    ans = "0"+ans
                elif a_arr[i] == "1" and b_arr[i] == "1":
                    ans = "0"+ans
                    carry_over = True
                else:
                    ans = "1"+ans
            i -= 1
        # Adding in the 1 infront if there is still a carry over 1 afer summing both binary numbers
        if carry_over:
            ans = "1"+ans
        return ans
