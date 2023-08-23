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
