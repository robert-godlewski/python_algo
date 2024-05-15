# Tools
from algo.datastructures.tools import titleline, thinline
from algo.solutions.binary_search_solutions import Solution


solver = Solution ()


# Main function to run all tests
def bsAlgorithms() -> None:
    titleline("Testing binary search algorithms")

    arrRand1 = [-1,0,3,4,9,12]
    bSearchTest(arrRand1,9)
    bSearchTest(arrRand1,2)
    bSearchTest([1],0)
    thinline()

    sqrtTest(4)
    sqrtTest(8)
    sqrtTest(0)
    sqrtTest(1)
    thinline()

    # arrRand2 = [4,5,6,7,0,1,2]
    # rSearchTest(arrRand2,0)
    # rSearchTest(arrRand2,3)
    # rSearchTest(arrRand2,5)
    # rSearchTest([1],0)
    # thinline()

    peakTest([1,2,3,1])
    peakTest([1,2,1,3,5,6,4])

# Testing bsearch
def bSearchTest(nums: list[int], target: int) -> None:
    print(f"Finding {target} in {nums}")
    answer = solver.bsearch(nums, target)
    print(f"The index is {answer}")

# Testing mySqrt
def sqrtTest(x: int) -> None:
    answer = solver.mySqrt(x)
    print(f"The Square Root of {x} = {answer}")

# Testing rsearch
def rSearchTest(nums: list[int], target: int) -> None:
    print(f"Finding {target} in {nums}")
    answer = solver.rsearch(nums, target)
    print(f"The index is {answer}")

# Testing findPeakElement
def peakTest(nums: list[int]) -> None:
    print(f"Finding the peak number in {nums}")
    answer = solver.findPeakElement(nums)
    print(f"Peak Element = {answer}")
