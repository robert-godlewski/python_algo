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


# Quick Sorting Algorithm: - Skip
# Space complexity = O(log(n))
# Average time complexity = O(nlog(n))
# Worst time complexity = O(n**2)
def quickSort(nums: list[int]) -> list[int]: return nums

# Testing out quick sorting algorithm
def quickTest() -> None:
    quick = [10,80,30,90,40,50,70]
    old_quick = quick[:]
    quick = quickSort(quick)
    print('Quick Sorted array:')
    sortTestPrint(old_quick,quick)


# Merge Sorting Algorithm:
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

# Radix Sorting Algorithm:

# Bucket Sorting Algorithm:

# Comb Sorting Algorithm:

# Shell Sorting Algorithm:

# Tree Sorting Algorithm:

# Cube Sorting Algorithm:

# Time Sorting Algorithm:

# Heap Sorting Algorithm:
