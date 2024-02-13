# Sorting algorithms are organized by easiest to hardest to learn

# Basic swapping function to switch and sort the arrays
# Both Space and Time Complexity of O(1)
def swapInts(nums: list[int], a: int, b: int) -> list[int]:
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp
    return nums

# Basic viewing to test out the sorting algorithms
def sortTestPrint(arr: list[int], new_arr: list[int]) -> None:
    print(f'Old array: {arr}')
    print(f'Sorted array: {new_arr}')


# Bubble Sorting Algorithm:
# The algorithm goes through an array and swaps 2 elements next to each other
# in the array ranking them minimum to maximum value.
# Space Complexity = O(1) 
# because the algortithm is only using constants to resort the array,
# not complex data structures.
# Time Complexity = O(n**2) 
# because we are making multiple passes of the same array with a nested loop.
def bubbleSortBasic(nums: list[int]) -> list[int]:
    for k in range(len(nums)-1):
        for i in range(len(nums)-1-k):
            if nums[i] > nums[i+1]:
                nums = swapInts(nums, i, i+1)
    return nums

# Bubble Sorting Algorithm (slightly quicker version)
# Space Complexity = O(1) for the same reasons prior
# Best Time Complexity = O(n) 
# because if we implement a flag at 0 as an indicator will cut down in time,
# 0 means that eveything has been checked and sorted.
# Average Time Complexity = O(n**2) 
# because we are still making multiple passes and 
# if flag > 0 then we still need to repeat the loop to sort everything
def bubbleSort(nums: list[int]) -> list[int]:
    for k in range(len(nums)-1):
        flag = 0
        for i in range(len(nums)-1-k):
            if nums[i] > nums[i+1]:
                nums = swapInts(nums, i, i+1)
                flag += 1
        if flag == 0:
            break
    return nums

# Testing out bubble sorting algorithm
def bubbleTest() -> None:
    bubble = [4,1,3,2]
    old_bubble = bubble[:]
    bubble = bubbleSort(bubble)
    print('Bubble Sort:')
    sortTestPrint(old_bubble,bubble)


# Selection Sorting Algorithm:
# The algorithm goes through an array and swaps 2 elements;
# the minimum value with the starting index of the loop currently working on.
# Space Complexity = O(1) 
# because the algortithm is only using constants to resort the array,
# not complex data structures.
# Time Complexity = O(n**2) 
# because we are making multiple passes of the same array with a nested loop.
def selectionSort(nums: list[int]) -> list[int]:
    for j in range(len(nums)-1):
        iMin = j
        i = j+1
        while i < len(nums):
            if nums[i] < nums[iMin]:
                iMin = i
            i += 1
        if iMin != j:
            nums = swapInts(nums, j, iMin)
    return nums

# Testing out selection sorting algorithm
def selectionTest() -> None:
    select = [4,1,3,2]
    old_select = select[:]
    select = selectionSort(select)
    print('Selection Sort:')
    sortTestPrint(old_select,select)


# Insertion Sorting Algorithm:
# The algorithm goes through an array and develops 2 sections while processing;
# the sorted section at the start of the array and compares items in the 
# unsorted section inserting unsorted items in the proper position.
# Space Complexity = O(1)
# because the algortithm is only using constants to resort the array,
# not complex data structures.
# Average Time Complexity = O(n^2)
# because we are making multiple passes of the same array with a nested loop.
# Best Time Complexity = O(n)
# because if there's barely any sorting necessary the algorithm would've only gone through the array once.
def insertSort(nums: list[int]) -> list[int]:
    i = 1
    while i < len(nums):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums = swapInts(nums, j, j-1)
            j -= 1
        i += 1
    return nums

# Testing out insertion sorting algorithm
def insertionTest() -> None:
    insert = [25,22,27,15,19]
    old_insert = insert[:]
    insert = insertSort(insert)
    print('Insert Sort:')
    sortTestPrint(old_insert,insert)


# Quick Sorting Algorithm:
# Space complexity = O(log(n))
# Average time complexity = O(nlog(n))
# Worst time complexity = O(n**2)
def quickSort(nums: list[int]) -> list[int]: 
    if len(nums) > 1:
        # find the pivot point in the array
        pivot = int(len(nums)/2)
        left_nums = nums[0:pivot]
        right_nums = nums[pivot+1:]
        # recursively sort through both sides of the pivot
        left_nums = quickSort(left_nums)
        right_nums = quickSort(right_nums)
        # combine the arrays back together
        i = 0
        l = 0
        r = 0
        pivNum = nums[pivot]
        while i < len(nums):
            if pivNum and l < len(left_nums) and r < len(right_nums):
                if pivNum > left_nums[l] and pivNum > right_nums[r]:
                    if left_nums[l] <= right_nums[r]:
                        nums[i] = left_nums[l]
                        l += 1
                    else:
                        nums[i] = right_nums[r]
                        r += 1
                elif pivNum <= left_nums[l] and pivNum <= right_nums[r]:
                    nums[i] = pivNum
                    pivNum = None
                else:
                    if pivNum > right_nums[r]:
                        nums[i] = right_nums[r]
                        r += 1
                    elif pivNum > left_nums[l]:
                        nums[i] = left_nums[l]
                        l += 1
            elif pivNum and l < len(left_nums):
                if pivNum <= left_nums[l]:
                    nums[i] = pivNum
                    pivNum = None
                else:
                    nums[i] = left_nums[l]
                    l += 1
            elif pivNum and r < len(right_nums):
                if pivNum <= right_nums[r]:
                    nums[i] = pivNum
                    pivNum = None
                else:
                    nums[i] = right_nums[r]
                    r += 1
            elif pivNum:
                nums[i] = pivNum
                pivNum = None
            else:
                if l < len(left_nums) and r < len(right_nums):
                    if left_nums[l] <= right_nums[r]:
                        nums[i] = left_nums[l]
                        l += 1
                    else:
                        nums[i] = right_nums[r]
                        r += 1
                elif l < len(left_nums):
                    nums[i] = left_nums[i]
                    l += 1
                elif r < len(right_nums):
                    nums[i] = right_nums[r]
                    r += 1
            i += 1
    return nums

# Testing out quick sorting algorithm
def quickTest() -> None:
    quick = [10,80,30,90,40,50,70]
    old_quick = quick[:]
    quick = quickSort(quick)
    print('Quick Sorted array:')
    sortTestPrint(old_quick,quick)


# Merge Sorting Algorithm:
# The algorithm recursively finds the middle of the array and 
# then compares 2 items in the array to sort least to greatest value.
# Space complexity = O(n)
# because the algorithm is recursively creating a temporary array every time.
# Time complexity = O(nlog(n))
# because the algorithm is using an inital loop and "mini" loops through recursion
# inorder to compare the items in the array.
def mergeSort(nums: list[int]) -> list[int]:
    if len(nums) > 1:
        mid = int(len(nums)/2)
        left_nums = nums[0:mid]
        right_nums = nums[mid:]
        left_nums = mergeSort(left_nums)
        right_nums = mergeSort(right_nums)
        l = 0
        r = 0
        i = 0
        while i < len(nums):
            if l < len(left_nums) and r < len(right_nums):
                if left_nums[l] <= right_nums[r]:
                    nums[i] = left_nums[l]
                    l += 1
                elif left_nums[l] > right_nums[r]:
                    nums[i] = right_nums[r]
                    r += 1
            elif l < len(left_nums):
                nums[i] = left_nums[l]
                l += 1
            elif r < len(right_nums):
                nums[i] = right_nums[r]
                r += 1
            i += 1
    return nums

# Testing out merge sorting algorithm
def mergeTest() -> None:
    merge = [16,19,14,20,12,13]
    old_merge = merge[:]
    merge = mergeSort(merge)
    print('Merge Sorted array:')
    sortTestPrint(old_merge,merge)

# Counting Sorting Algorithm:
# The algorithm first finds the maximum number value within the array,
# then creates a new array from the max number + 1 (for 0) to track
# how many times each number from 0-max is present in the array,
# lastly we loop through both arrays and making everything in the counting array
# as 0 and sort out everything in the original array.
# Space complexity = O(k)
# because of the introduction of an entirely separate array as a counter.
# Time complexity = O(n+k)
# because of looping through both the main array and the counter array.
def countingSort(nums: list[int]) -> list[int]:
    # Find the maximum number in the array
    maxInt = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] > maxInt:
            maxInt = nums[i]
        i += 1
    # Create an index system of each number up to the max
    counts = [0 for _ in range(maxInt+1)]
    i = 0
    while i < len(nums):
        counts[nums[i]] += 1
        i += 1
    # Properly put each item in the correct order
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

# Testing out counting sorting algorithm
def countingTest() -> None:
    counting = [1,0,3,1,3,1]
    old_counting = counting[:]
    counting = countingSort(counting)
    print('counting Sorted array:')
    sortTestPrint(old_counting,counting)

# Radix Sorting Algorithm:
# ...
# Space Complexity = O(n+k)
# ...
# Time Complexity = O(nk)
# ...
def radixSort(nums: list[int]) -> list[int]:
    '''
    main
    ___var____|_val
    nums      | [53, 89, 150, 36, 633, 233] => ... => [36,53,89,150,233,633]
    maxLen    | 0 => 2 => 3
    strNums   | [] => ... => [['5','3'],
        ['8','9'],
        ['1','5','0'],
        ['3','6'],
        ['6','3','3'],
        ['2','3','3']] => ... => [['0','5','3'],
        ['0','8','9'],
        ['1','5','0'],
        ['0','3','6'],
        ['6','3','3'],
        ['2','3','3']] => [['1','5','0'],
        ['0','5','3'],
        ['6','3','3'],
        ['2','3','3'],
        ['0','3','6'],
        ['0','8','9']] => [['6','3','3'],
        ['2','3','3'],
        ['0','3','6'],
        ['1','5','0'],
        ['0','5','3'],
        ['0','8','9']] => [['0','3','6'],
        ['0','5','3'],
        ['0','8','9'],
        ['1','5','0'],
        ['2','3','3']
        ['6','3','3']]
    num       | 53 -> 89 -> ...
    numStrArr | str(53).split("") -> "53".split("") -> ['5','3'] -> ...
    i         | 0 => ...
    r         | 2 -> 1 -> 0 -> -1
    j         | 0 => ...
    temp      | '' => '36' => ...
    '''
    print(f'Nums in = {nums}')
    # Getting the maximum length for all numbers
    maxLen = 0
    strNums = []
    for num in nums:
        print(num)
        numStrArr = list(str(num))
        if len(numStrArr) > maxLen:
            maxLen = len(numStrArr)
        strNums.append(numStrArr)
    print(strNums)
    # Adjusting the smaller numbers to fit in with the bigger ones
    i = 0
    while i < len(strNums):
        if len(strNums[i]) != maxLen:
            strNums[i].insert(0,'0')
        else: 
            i += 1
    # Count sort the whole array
    def radixCountingSort(arr: list[list[str]], r: int) -> list[list[str]]:
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
    
    r = maxLen-1
    while r >= 0:
        strNums = radixCountingSort(strNums,r)
        r -= 1
    # Convert the list[list[str]] to a list[int]
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

# Testing out radix sorting algorithm
def radixTest() -> None:
    radix = [53, 89, 150, 36, 633, 233]
    old_radix = radix[:]
    radix = radixSort(radix)
    print('radix sorted array:')
    sortTestPrint(old_radix,radix)

# Bucket Sorting Algorithm:

# Comb Sorting Algorithm:

# Shell Sorting Algorithm:

# Tree Sorting Algorithm:

# Cube Sorting Algorithm:

# Time Sorting Algorithm:

# Heap Sorting Algorithm:
