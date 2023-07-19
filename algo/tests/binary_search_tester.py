# Tools
from algo.datastructures.tools import titleline, thinline
from algo.solutions.binary_search_solutions import Solution


solver = Solution ()


# Main function to run all tests
def bsAlgorithms() -> None:
    titleline("Testing binary search algorithms")

    bSearchTest([-1,0,3,5,9,12],9)
    bSearchTest([-1,0,3,5,9,12],2)
    bSearchTest([4,5,6,7,0,1,2],0)
    bSearchTest([4,5,6,7,0,1,2],3)
    bSearchTest([1],0)
    thinline()

    sqrtTest(4)
    sqrtTest(8)

# Testing search
def bSearchTest(nums: list[int], target: int) -> None:
    print(f"Finding {target} in {nums}")
    answer = solver.search(nums, target)
    print(f"The index is {answer}")

# Testing mySqrt
def sqrtTest(x: int) -> None:
    answer = solver.mySqrt(x)
    print(f"The Sqare Root of {x} = {answer}")

