# Tools needed
from algo.datastructures.tools import titleline, thinline
from algo.solutions.recursion2_solutions import Solution


solver = Solution()


# Main function to run all tests
def recursion2Algorithms() -> None:
    titleline("Testing recursion group 2 algorithms")

    mergeSortTest([5,2,3,1])
    mergeSortTest([5,1,1,2,0,0])
    thinline()

    matrix = [
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]
    ]
    searchMatrixTest(matrix, 5)
    searchMatrixTest(matrix, 20)


# Testing sortArray - Based off of a merge sorting algorithm
def mergeSortTest(nums: list[int]) -> None:
    print(f"Sorting {nums} in order:")
    ans = solver.sortArray(nums)
    print(f"Sorted = {ans}")

# Testing searchMatrix
def searchMatrixTest(matrix: list[list[int]], target: int) -> None:
    ans = solver.searchMatrix(matrix, target)
    print(f"Is {target} in {matrix}? {ans}")
