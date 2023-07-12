# Solutions solved  in July 2022 - Sept 2022
class Solution:
    # Do not return anything, modify arr in-place instead.
    # Solved under 30 min
    def duplicateZeros(self, arr):
        #print(f"arr in = [{arr}]")
        i = 0
        while i < len(arr): # true
            #print(f"arr = [{arr}]")
            #print(f"i = {i}")
            #print(f"arr[i] = {arr[i]}")
            if arr[i] == 0: # true
                arr.insert(i, 0)
                arr.pop()
                i += 1
            i += 1
        # Don't add this to leet code
        return arr
    
    # Do not return anything, modify nums1 in-place instead. - Usual O(n), Best O(1) solution
    # solved in an hour - need to practice
    def merge(self, nums1, m, nums2, n):
        #print(f"nums1 = {nums1}")
        #print(f"m = {m}")
        #print(f"nums2 = {nums2}")
        #print(f"n = {n}")
        # combining both arrays
        #print("Combining nums1 and nums2")
        length = m+n
        i = m
        j = 0
        while i < length:
            #print(f"nums1[{i}] = {nums1[i]}")
            #print(f"nums2[{j}] = {nums2[j]}")
            nums1[i] = nums2[j]
            i += 1
            j += 1
        #print(f"nums1 = {nums1}")
        # sorting nums1
        #print("sorting nums1")
        nums1 = self.mergeSort(nums1)
        #print(f"returning {nums1}")
        # Don't add this to leetcode
        return nums1
    
    # part of merge algorithm - found most on Geeks for Geeks online
    def mergeSort(self, arr):
        #print(f"arr in = {arr}")
        if len(arr) > 1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            left = self.mergeSort(left)
            right = self.mergeSort(right)
            i = 0
            j = 0
            k = 0
            # sorting the 2 together
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            # adding in all of the remaining left side
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            # adding in all of the remaining right side
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        return arr

    # O(n) solution - Complex solution
    # Solved within 30 min - Need to practice, initially misunderstood what they were asking
    '''
    def removeElement(self, nums, val):
        #print(f"List in = {nums}")
        #print(f"Removing all {val} from nums")
        k = 0
        i = 0
        while i < len(nums):
            #print(f"current num is {nums[i]}")
            if nums[i] == val:
                nums[i] = '_'
            else: k += 1
            i += 1
        #print(f"Array removing {val} = {nums}")
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] != '_': i+=1
            elif nums[j] == '_': j -= 1
            elif nums[j] != '_':
                nums[i] = nums[j]
                nums[j] = '_'
        print(f"Array with _ at the end = {nums}")
        return k
    '''

    # Simplified solution but still O(n)
    def removeElement(self, nums, val):
        #print(f"nums in = {nums}")
        while val in nums:
            nums.remove(val)
            #print(f"nums = {nums}")
        #print(f"nums out = {nums}")
        return len(nums)

    # nums is sorted - O(n) solution
    # solved within 10 min
    def removeDuplicates(self, nums):
        print(f"nums in = {nums}")
        temp = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == temp: nums.pop(i)
            else:
                temp = nums[i]
                i += 1
        print(f"nums out = {nums}")
        return len(nums)

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

    # Binary addition
    # binary numbers are in 2 strings
    # returns a string
    # Solved in - about 1 hr, need help figuring out binary addition
    def addBinary(self, a, b):
        print(a)
        print(b)
        # get both of the strings to have equal length
        while len(a) != len(b):
            if len(a) > len(b): 
                b = "0" + b
            elif len(a) < len(b): 
                a = "0" + a
        print(f"Binary adding {a} + {b}")
        a_arr = list(a)
        print(a_arr)
        b_arr = list(b)
        print(b_arr)
        total = ""
        # need this boolean to determine if there is a 1 to carry over
        carry = False
        while len(a_arr) > 0 and len(b_arr) > 0:
            bin1 = a_arr.pop()
            bin2 = b_arr.pop()
            print(f"{bin1} + {bin2}")
            if carry:
                if bin1 == bin2:
                    total = "1" + total
                    if bin1 == "0":
                        carry = False
                else:
                    total = "0" + total
            else:
                if bin1 == bin2:
                    total = "0" + total
                    if bin1 == "1":
                        carry = True
                    else:
                        carry = False
                elif bin1 != bin2:
                    total = "1" + total
        # if there is still a 1 to carry over we add it
        if carry:
            total = "1" + total
        return total

    # haystack and needle are both str
    # returns an int based off of the index needle starts is in haystack
    # Solution in - 30 min - Doesn't work
    # Most cases: O(n**2)
    # Best case: O(1)
    def strStr(self, haystack, needle):
        # Base Cases
        if len(needle) < 1:
            return 0
        elif len(haystack) == len(needle) and haystack == needle:
            return 0
        # creating a comparison variable based from haystack
        i = 0
        arr = list(haystack)
        comp = []
        while i < len(needle):
            comp.append(arr[i])
            i += 1
        # Finding the index
        i = 0
        while i < len(haystack):
            temp = ""
            for j in comp:
                temp += j
            print(f"comparing {temp} to {needle}")
            if temp == needle:
                print("found")
                return i
            else:
                print("not found")
            hayind = len(comp) + i
            if hayind >= len(haystack) - 1:
                break
            comp.pop(0)
            comp.append(arr[hayind])
            i += 1
        # if not fround an index
        return -1

    # strs is a list of str
    # returns a str
    # Solution in - 30 min
    def longestCommonPrefix(self, strs):
        print("List of strs:")
        print(strs)
        # Base case
        if len(strs) == 1:
            return strs[0]
        # converting each string to a list of strings
        i = 0
        words = len(strs)
        while i < words:
            li = list(strs[i])
            strs[i] = li
            i += 1
        print("listify strs:")
        print(strs)
        # checking
        compre = ""
        is_in_all = False
        i = 0
        while i < len(strs[0]):
            letter = strs[0][i]
            c = 1
            while c < words:
                if i >= len(strs[c]):
                    is_in_all = False
                    break
                temp = strs[c][i]
                if temp == letter:
                    is_in_all = True
                else:
                    is_in_all = False
                    break
                c += 1
            if not is_in_all:
                break
            compre += letter
            is_in_all = False
            i += 1
        return compre

    # s is a list of str
    # returns None in leetcode
    # will return s
    # Solved in 10 min
    # O(n)
    def reverseString(self, s):
        # Do not return anything, modify s in-place instead.
        i = 0
        while i < len(s)//2:
            temp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = temp
            i += 1
        return s

    # nums is a list of int (always an even length)
    # finds the min of every possible pair and returns the max sum
    # Solved in 30 min but not optimal, times out in leetcode
    '''
    def arrayPairSum(self, nums):
        if len(nums)//2 == 1:
            return min(nums[0], nums[1])
        # sorting
        arr = []
        i = 0
        while i < len(nums):
            temp = min(nums)
            arr.append(temp)
            nums.remove(temp)
        print(arr)
        # grabbing the optimal sums
        sums = []
        while i < len(arr):
            temp = arr[i]
            sums.append(temp)
            i += 2
        # finding out the sum
        maxnum = 0
        for s in sums:
            maxnum += s
        return maxnum
    '''
    # Solution 1 - In leetcode
    '''
    def arrayPairSum(self, nums):
        # Sort the list in ascending order
        nums.sort()
        # Initialize sum to zero
        max_sum = 0
        for i in range(0, len(nums), 2):
            # Add every element at even positions (0-indexed)
            max_sum += nums[i]
        return max_sum
    '''
    # Solution 2 - In leetcode
    def arrayPairSum(self, nums):
        # upper end of possible values
        K = 10000
        # Store the frequency of each element
        element_to_count = [0] * (2 * K + 1)
        for element in nums:
            # Add K to element to offset negative values
            element_to_count[element + K] += 1
        # Initialize sum to zero
        max_sum = 0
        is_even_index = True
        for element in range(2 * K + 1):
            while element_to_count[element] > 0 :
                # Add element if it is at even index
                if is_even_index:
                    max_sum += element - K
                # Flip the value (one to zero or zero to one)
                is_even_index = not is_even_index
                # Decrement the frequency count
                element_to_count[element] -= 1
        return max_sum

    # numbers is a list of int and target is an int that 2 indecies add up to
    # returns a list of int
    # Solution in 20 min - Solution is wrong in leetcode due to time limit exceeded but not sure
    def twoSum(self, numbers, target):
        # base cases
        if len(numbers) < 2 or len(numbers) > 3 * (10**4):
            return [0,0]
        arr = []
        i = 0
        while i < len(numbers):
            j = i+1
            while j < len(numbers):
                print(f"does {numbers[i]} + {numbers[j]} = {target}?")
                if numbers[i] + numbers[j] == target:
                    print("Yes")
                    arr.append(i+1)
                    arr.append(j+1)
                    break
                else:
                    print("No")
                j += 1
            if len(arr) > 0:
                break
            i += 1
        return arr
