# Sorting algorithms are organized by easiest to hardest to learn
class Sorter:
    def _swapInts(self, nums: list[int], a: int, b: int) -> list[int]:
        # Basic swaping function to switch the position of a with b in nums
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp
        return nums

    def bubbleSortBasic(self, nums: list[int]) -> list[int]:
        # Basic version of the Bubble Sort Algorithm
        for k in range(len(nums)-1):
            for i in range(len(nums)-1-k):
                if nums[i] > nums[i+1]:
                    nums = self._swapInts(nums, i, i+1)
        return nums

    def bubbleSort(self, nums: list[int]) -> list[int]:
        # Slightly quicker version of the Bubble Sort Algorithm
        for k in range(len(nums)-1):
            flag = 0
            for i in range(len(nums)-1-k):
                if nums[i] > nums[i+1]:
                    nums = self._swapInts(nums, a=i, b=i+1)
                    flag += 1
            if flag == 0:
                break
        return nums

    def selectionSort(self, nums: list[int]) -> list[int]:
        for j in range(len(nums)-1):
            # iMin is the proposed index of the minimum value
            iMin = j
            i = j+1
            while i < len(nums):
                if nums[i] < nums[iMin]:
                    iMin = i
                i += 1
            if iMin != j:
                nums = self._swapInts(nums, j, iMin)
        return nums

    def insertSort(self, nums: list[int]) -> list[int]:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and nums[j-1] > nums[j]:
                nums = self._swapInts(nums, j, j-1)
                j -= 1
            i += 1
        return nums

    def quickSort(self, nums: list[int], left: int=-1, right: int=-1) -> list[int]:
        # left and right variables are useful as pointers for the start and ending points to sort in the array
        if left == -1 and right == -1:
            left = 0
            right = len(nums)-1
        if left < right:
            pivot = self._quickPartition(nums, left, right)
            nums = self.quickSort(nums, left, pivot-1)
            nums = self.quickSort(nums, pivot+1, right)
        return nums

    def _quickPartition(self, nums: list[int], left: int, right: int) -> int:
        # Part of the Quick Sort algorithm to find the pivot index to use
        i = left
        j = right-1
        while i < j:
            while i < right and nums[i] < nums[right]:
                i += 1
            while j > left and nums[j] >= nums[right]:
                j -= 1
            if i < j:
                nums = self._swapInts(nums, i, j)
        if nums[i] > nums[right]:
            nums = self._swapInts(nums, i, right)
        return i

    def mergeSort(self, nums: list[int]) -> list[int]:
        # This is the base called function to merge sort nums
        if len(nums) > 1:
            mid = int(len(nums)/2)
            left_nums = nums[0:mid]
            right_nums = nums[mid:]
            left_nums = self.mergeSort(left_nums)
            right_nums = self.mergeSort(right_nums)
            nums = self._merge2intoOne(nums, left_nums, right_nums)
        return nums

    def _merge2intoOne(self, nums: list[int], left: list[int], right: list[int]) -> list[int]:
        # Compare the sorted left and right arrays and put in place into nums
        l = 0
        r = 0
        i = 0
        while i < len(nums) and l < len(left) and r < len(right):
            if left[l] <= right[r]:
                nums[i] = left[l]
                l += 1
            else:
                # left[l] > right[r]
                nums[i] = right[r]
                r += 1
            i += 1
        # Add in the remaining of either left or right into nums
        while i < len(nums) and l < len(left):
            nums[i] = left[l]
            l += 1
            i += 1
        while i < len(nums) and r < len(right):
            nums[i] = right[r]
            r += 1
            i += 1
        return nums

    def countingSort(self, nums: list[int]) -> list[int]:
        # This is the base of the counting sort algorithm
        maxInt = self._findCountMax(nums)
        counts = self._createCountArr(nums, maxInt)
        return self._positionCountSort(nums, counts, maxInt)

    def _findCountMax(self, nums: list[int]) -> int:
        # Finds and returns the maximum number in the array
        maxInt = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] > maxInt:
                maxInt = nums[i]
            i += 1
        return maxInt

    def _createCountArr(self, nums: list[int], length: int) -> list[int]:
        # Creates an index system for each number up to the given length
        counts = [0 for _ in range(length+1)]
        i = 0
        while i < len(nums):
            counts[nums[i]] += 1
            i += 1
        return counts

    def _positionCountSort(self, nums: list[int], counts: list[int], maxInt: int) -> list[int]:
        # Properly put everything from counts into nums
        j = 0
        i = 0
        while i < len(nums) and j <= maxInt:
            if counts[j] > 0:
                nums[i] = j
                counts[j] -= 1
                i += 1
            else:
                j += 1
        return nums

    def bucketSort(self, nums: list[int]) -> list[int]:
        # 1. Make the buckets
        max_int = self._findCountMax(nums)
        size = max_int/len(nums)
        buckets = self._createBuckets(nums, size)
        #2. Sort the buckets
        buckets = self._sortBuckets(buckets)
        # 3. Put data in the buckets back into nums
        return self._positionBuckets(nums, buckets)

    def _createBuckets(self, nums: list[int], size: float) -> list[list[int]]:
        buckets = [[] for _ in range(len(nums))]
        for num in nums:
            i = int(num/size)
            if i != len(nums) and i < len(nums):
                buckets[i].append(num)
            else:
                buckets[len(nums)-1].append(num)
        return buckets

    def _sortBuckets(self, buckets: list[list[int]]) -> list[list[int]]:
        for bucket in buckets:
            if len(bucket) >= 2:
                # We will sort the bucket array with something that doesn't require extra space
                bucket = self.bubbleSort(bucket)
        return buckets

    def _positionBuckets(self, nums: list[int], buckets: list[list[int]]):
        n = 0 # index for nums
        b = 0 # index for buckets
        while n < len(nums) and b < len(buckets):
            for num in buckets[b]:
                nums[n] = num
                n += 1
            b += 1
        return nums

    # Radix Sorting Algorithm: - Fix this
    # ...
    # Space Complexity = O(n+k)
    # ...
    # Time Complexity = O(nk)
    # ...
    def _radixCountingSort(arr: list[list[str]], r: int) -> list[list[str]]:
        # Count sort the whole array after splitting it up at the rth index
        # count sorts arr off of r
        maxInt = int(arr[0][r])
        counts = {arr[0][r]: [arr[0]]}
        i = 1
        while i < len(arr):
            if arr[i][r] in counts:
                counts[arr[i][r]].append(arr[i])
            else:
                counts[arr[i][r]] = [arr[i]]
            num = int(arr[i][r])
            if num > maxInt:
                maxInt = num
            i += 1
        i = 0
        j = 0
        while i < len(arr) and j <= maxInt:
            key = str(j)
            if key in counts:
                if len(counts[key]) > 0:
                    arr[i] = counts[key].pop(0)
                    i += 1
                else:
                    j += 1
            else:
                j += 1
        return arr

    def radixSort(self, nums: list[int]) -> list[int]:
        # Getting the maximum length for all numbers
        maxLen = 0
        strNums = []
        for num in nums:
            numStrArr = list(str(num))
            if len(numStrArr) > maxLen:
                maxLen = len(numStrArr)
            strNums.append(numStrArr)
        # Adjusting the smaller numbers to fit in with the bigger ones
        i = 0
        while i < len(strNums):
            if len(strNums[i]) != maxLen:
                strNums[i].insert(0,'0')
            else: 
                i += 1
        # Counting sort each index
        r = maxLen-1
        while r >= 0:
            strNums = self._radixCountingSort(strNums,r)
            r -= 1
        # Add and convert strNums back into nums
        i = 0
        while i < len(strNums):
            j = 0
            temp = ''
            while j < len(strNums[i]):
                if strNums[i][j] == '0' and j == 0:
                    strNums[i].pop(0)
                else:
                    temp += strNums[i][j]
                    j += 1
            nums[i] = int(temp)
            i += 1
        return nums

    # Other sorting algorithms go here....

    # Comb Sorting Algorithm:

    # Shell Sorting Algorithm:

    # Tree Sorting Algorithm:

    # Cube Sorting Algorithm:

    # Time Sorting Algorithm:

    # Heap Sorting Algorithm:


class SortTests:
    def __init__(self):
        self.sorter = Sorter()

    # Testing out bubble sorting algorithm
    def _bubbleTest(self, bubble: list[int]) -> None:
        old_bubble = bubble[:]
        bubble = self.sorter.bubbleSort(bubble)
        print('Bubble Sort:')
        self._sortTestPrint(old_bubble,bubble)

    # Testing out selection sorting algorithm
    def _selectionTest(self, select: list[int]) -> None:
        old_select = select[:]
        select = self.sorter.selectionSort(select)
        print('Selection Sort:')
        self._sortTestPrint(old_select,select)

    # Testing out insertion sorting algorithm
    def _insertionTest(self, insert: list[int]) -> None:
        old_insert = insert[:]
        insert = self.sorter.insertSort(insert)
        print('Insert Sort:')
        self._sortTestPrint(old_insert,insert)

    # Testing out quick sorting algorithm
    def _quickTest(self, quick: list[int]) -> None:
        old_quick = quick[:]
        quick = self.sorter.quickSort(quick)
        print('Quick Sorted array:')
        self._sortTestPrint(old_quick,quick)

    # Testing out merge sorting algorithm
    def _mergeTest(self, merge: list[int]) -> None:
        old_merge = merge[:]
        merge = self.sorter.mergeSort(merge)
        print('Merge Sorted array:')
        self._sortTestPrint(old_merge,merge)

    # Testing out counting sorting algorithm
    def _countingTest(self, counting: list[int]) -> None:
        old_counting = counting[:]
        counting = self.sorter.countingSort(counting)
        print('counting Sorted array:')
        self._sortTestPrint(old_counting,counting)

    # Testing out bucket sorting algorithm
    def _bucketTest(self, bucket: list[int]) -> None:
        old_bucket = bucket[:]
        bucket = self.sorter.bucketSort(bucket)
        print('bucket sorted array:')
        self._sortTestPrint(old_bucket,bucket)

    # Testing out radix sorting algorithm
    def _radixTest(self, radix: list[int]) -> None:
        old_radix = radix[:]
        radix = self.sorter.radixSort(radix)
        print('radix sorted array:')
        self._sortTestPrint(old_radix,radix)

    # Other Tests go here....
    def _sortTestPrint(self, old_arr: list[int], new_arr: list[int]) -> None:
        # Basic viewing to test out the sorting algorithms
        print(f'Old array: {old_arr}')
        print(f'Sorted array: {new_arr}')

def runSortingTests():
    tester = SortTests()
    tester._bubbleTest([4,1,3,2])
    tester._selectionTest([4,1,3,2])
    tester._insertionTest([25,22,27,15,19])
    tester._quickTest([10,80,30,90,40,50,70])
    tester._mergeTest([16,19,14,20,12,13])
    tester._countingTest([1,0,3,1,3,1])
    tester._bucketTest([38, 27, 43, 3, 9, 10])
    # tester._radixTest([53, 89, 150, 36, 633, 233])
