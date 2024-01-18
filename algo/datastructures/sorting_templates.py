# Basic swapping function to switch and sort the arrays
# Both Space and Time Complexity of O(1)
def swapInts(nums: list[int], a: int, b: int) -> list[int]:
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp
    return nums


# Quick Sorting Algorithm:

# Merge Sorting Algorithm:

# Time Sorting Algorithm:

# Heap Sorting Algorithm:


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
    print(f'Old array: {bubble}')
    bubble = bubbleSort(bubble)
    print(f'Bubble Sorted array: {bubble}')


# Insertion Sorting Algorithm:
# The algorithm goes through an array and swaps 2 elements ranking them minimum to maximum value.
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
    insert = [4,1,3,2]
    print(f'Old array: {insert}')
    insert = insertSort(insert)
    print(f'Insert Sorted array: {insert}')


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
    print(f'Old array: {select}')
    select = selectionSort(select)
    print(f'Selection Sorted array: {select}')


# Tree Sorting Algorithm:

# Shell Sorting Algorithm:

# Bucket Sorting Algorithm:

# Radix Sorting Algorithm:

# Counting Sorting Algorithm:

# Cube Sorting Algorithm:
