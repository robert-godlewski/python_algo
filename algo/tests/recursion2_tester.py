# Tools needed
from algo.datastructures.tools import titleline, thinline
from algo.solutions.recursion2_solutions import Solution


solver = Solution()


# Main function to run all tests
def recursion2Algorithms() -> None:
    titleline("Testing recursion group 2 algorithms")

    mergeSortTest([5,2,3,1])
    mergeSortTest([5,1,1,2,0,0])


# Testing sortArray - Based off of a merge sorting algorithm
def mergeSortTest(nums: list[int]) -> None:
    print(f"Sorting {nums} in order:")
    ans = solver.sortArray(nums)
    print(f"Sorted = {ans}")
