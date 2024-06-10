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
    thinline()

    minTest([3,4,5,1,2])
    minTest([4,5,6,7,0,1,2])
    minTest([11,13,15,17])
    minTest([1])
    thinline()

    range_arr1 = [5,7,7,8,8,10]
    srTest(range_arr1,8)
    srTest(range_arr1,6)
    srTest([1],1)
    srTest([2,2],2)
    srTest([1,3],1)
    srTest([1,4],4)
    srTest([],0)

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

# Testing findMin
def minTest(nums: list[int]) -> None:
    print(f"Finding the minimum number in {nums}")
    answer = solver.findMin(nums)
    print(f"Minimum number = {answer}")

# Testing searchRange
def srTest(nums:list[int],target:int) -> None:
    print(f"Finding {target}'s in {nums}")
    answer = solver.searchRange(nums,target)
    print(f"The starting index = {answer[0]}")
    print(f"The ending index = {answer[1]}")
