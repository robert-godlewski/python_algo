# Tools needed
from algo.datastructures.tools import titleline, thinline
from algo.solutions.array_solutions import Solution


solver = Solution()


# Main function to run all tests
def arrayAlgorthims() -> None:
    titleline("Testing Array Algorithms")

    duplicateZerosTest([1,0,2,3,0,4,5,0])
    duplicateZerosTest([1,2,3])
    thinline()

    mergeArrTest([1,2,3,0,0,0], 3, [2,5,6], 3)
    mergeArrTest([1], 1, [], 0)
    mergeArrTest([0], 0, [1], 1)
    mergeArrTest([4,5,6,0,0,0], 3, [1,2,3], 3)
    thinline()

    removeElementTest([3,2,2,3], 3)
    removeElementTest([0,1,2,2,3,0,4,2], 2)
    thinline()

    removeDuplicatesTest([1,1,2])
    removeDuplicatesTest([0,0,1,1,1,2,2,3,3,4])


# Testing duplicateZeros
def duplicateZerosTest(arr: list[int]) -> None:
    print("Finding any 0's in an array and duplicating it them")
    print(f"Original = {arr}")
    arr_dup = solver.duplicateZeros(arr)
    print(f"Duplicated = {arr_dup}")


# Testing merge
def mergeArrTest(arr1: list[int], m: int, arr2: list[int], n: int) -> None:
    print(f"Merging {arr1} and {arr2}")
    merged_arr = solver.merge(arr1, m, arr2, n)
    print(merged_arr)


# Testing removeElement
def removeElementTest(arr: list[int], num: int) -> None:
    print(f"Removing {num} from {arr}")
    rem_arr = solver.removeElement(arr, num)
    print(f"Remaining numbers = {rem_arr}")


# Testing removeDuplicates
def removeDuplicatesTest(arr: list[int]) -> None:
    print(f"Removing duplicates in {arr}")
    remain = solver.removeDuplicates(arr)
    print(f"Remaining values = {remain}")
