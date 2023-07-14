# Tools needed
from algo.datastructures.tools import titleline, thinline
from algo.solutions.hashset_solutions import Solution


solver = Solution()


# Main function to run all tests
def hashsetAlgorithms() -> None:
    titleline("Testing hashset algorithms")

    containsDuplicateTest([1,2,3,1])
    containsDuplicateTest([1,2,3,4])
    containsDuplicateTest([1,1,1,3,3,4,3,2,4,2])
    thinline()

    singleNumberTest([2,2,1])
    singleNumberTest([4,1,2,1,2])
    singleNumberTest([1])
    thinline()

    intersectionTest([1,2,2,1],[2,2])
    intersectionTest([4,9,5],[9,4,9,8,4])
    thinline()

    isHappyTest(19)
    isHappyTest(2)
    isHappyTest(7)


# Testing containsDuplicate
def containsDuplicateTest(nums: list[int]) -> None:
    print(f"Looking for duplicates in {nums}")
    answer = solver.containsDuplicate(nums)
    print(f"Does this array contain any duplicates? {answer}")


# Testing singleNumber
def singleNumberTest(nums: list[int]) -> None:
    print(f"Looking for numbers without a duplicate in {nums}")
    answer = solver.singleNumber(nums)
    print(f"The single number = {answer}")


# Testing intersection
def intersectionTest(nums1: list[int], nums2: list[int]) -> None:
    print("Finding the intesection of:")
    print(nums1)
    print(nums2)
    answer = solver.intersection(nums1, nums2)
    print(f"Intersection = {answer}")


# Testing isHappy
def isHappyTest(num: int) -> None:
    answer = solver.isHappy(num)
    print(f"Is {num} a happy number? {answer}")
