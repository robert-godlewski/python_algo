# Basic swapping function to switch and sort the arrays
def swapInts(nums: list[int], a: int, b: int) -> list[int]:
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp
    return nums

# Basic Bubble Sorting Algorithm 
# where it goes through an array and swaps 2 elements in the array
# if it passes the condition.
# Space Complexity = O(1) because we are just resorting the same array
# Time Complexity = O(n**2) because we are making multiple passes
def bubbleSortBasic(nums: list[int]) -> list[int]:
    k = 1
    while k < len(nums):
        i = 0
        while i < len(nums)-k:
            if nums[i] > nums[i+1]:
                # temp = nums[i]
                # nums[i] = nums[i+1]
                # nums[i+1] = temp
                nums = swapInts(nums, i, i+1)
            i += 1
        k += 1
    return nums

# A slighly quicker Bubble Sorting Algorithm
# Using flag to see if everything is already sorted 1 time 
# because we don't need to look further before k goes to the end
# Space Complexity = O(1) because we are just resorting the array
# Time Complexity = O(n**2) because we are still making multiple passes
def bubbleSort(nums: list[int]) -> list[int]:
    k = 1
    while k < len(nums):
        i = 0
        flag = 0
        while i < len(nums)-k:
            if nums[i] > nums[i+1]:
                # temp = nums[i]
                # nums[i] = nums[i+1]
                # nums[i+1] = temp
                nums = swapInts(nums, i, i+1)
                flag += 1
            i += 1
        if flag == 0:
            break
        k += 1
    return nums

# Testing out bubble sorting functions
def bubbleTest() -> None:
    bubble = [4,1,3,2]
    print(f'Old array: {bubble}')
    bubble = bubbleSort(bubble)
    print(f'Bubble Sorted array: {bubble}')


# Selection Sorting Algorithm
# where it goes through an array and swaps the minimum value with the first index of the array it's working on.
# Space Complexity = O(1) because we are just resorting the array
# Time Complexity = O(n**2) because we are making multiple passes to go through each index of the array
def selectionSort(nums: list[int]) -> list[int]:
    j = 0
    while j < len(nums):
        iMin = j
        i = j+1
        while i < len(nums):
            if nums[i] < nums[iMin]:
                iMin = i
            i += 1
        if iMin != j:
            # temp = nums[iMin]
            # nums[iMin] = nums[j]
            # nums[j] = temp
            nums = swapInts(nums, j, iMin)
        j += 1
    return nums

# Testing out selection sorting functions
def selectionTest() -> None:
    select = [4,1,3,2]
    print(f'Old array: {select}')
    select = selectionSort(select)
    print(f'Selection Sorted array: {select}')
