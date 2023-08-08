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
    mergeArrTest([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3)
    thinline()

    removeElementTest([3,2,2,3], 3)
    removeElementTest([0,1,2,2,3,0,4,2], 2)
    thinline()

    removeDuplicatesTest([1,1,2])
    removeDuplicatesTest([0,0,1,1,1,2,2,3,3,4])
    thinline()

    mountArrTest([2,1])
    mountArrTest([3,5,5])
    mountArrTest([0,3,2,1])
    mountArrTest([2])
    mountArrTest([0,1,2,3])
    thinline()

    replaceETests([17,18,5,4,6,1])
    replaceETests([400])
    thinline()

    moveZeroesTest([0,1,0,3,12])
    moveZeroesTest([0])
    thinline()

    paritySortTest([3,1,2,4])
    paritySortTest([0])
    thinline()

    # pivotIndexTest([1,7,3,6,5,6])
    # pivotIndexTest([1,2,3])
    # pivotIndexTest([2,1,-1])
    # thinline()

    # dominantIndexTest([3,6,1,0])
    # dominantIndexTest([1,2,3,4])
    # thinline()

    # plusOneTest([1,2,3])
    # plusOneTest([4,3,2,1])
    # plusOneTest([9])
    # thinline()

    # findDiagonalOrderTest([[1,2,3],[4,5,6],[7,8,9]])
    # findDiagonalOrderTest[[1,2],[3,4]]
    # thinline()

    # spiralOrderTest([[1,2,3],[4,5,6],[7,8,9]])
    # spiralOrderTest([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    # spiralOrderTest([[3],[2]])
    # thinline()

    # generatePascalTest(5)
    # generatePascalTest(1)
    # thinline()

    # binarySumTest("11", "1")
    # binarySumTest("1010", "1011")
    # thinline()

    # findStrTest("hello", "ll")
    # findStrTest("aaaaa", "bba")
    # findStrTest("a", "a")
    # findStrTest("abc", "c")
    # thinline()

    # longestCommonPrefixTest(["flower","flow","flight"])
    # longestCommonPrefixTest(["dog","racecar","car"])
    # thinline()

    # reverseStringTest(['h','e','l','l','o'])
    # reverseStringTest(['H','a','n','n','a','h'])
    # thinline()

    # arrayPairSumTest([1,4,3,2])
    # arrayPairSumTest([6,2,6,5,1,2])
    # thinline()

    # twoSumTest([2,7,11,15], 9)
    # twoSumTest([2,3,4], 6)
    # twoSumTest([-1,0], -1)


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

# Testing validMountainArray
def mountArrTest(arr: list[int]) -> None:
    print(f"List = {arr}")
    answer = solver.validMountainArray(arr)
    print(f"Is the list a mountain array? {answer}")

# Testing replaceElements
def replaceETests(arr: list[int]) -> None:
    print(f"Original array = {arr}")
    answer = solver.replaceElements(arr)
    print(f"Adjusted array = {answer}")

# Testing moveZeroes
def moveZeroesTest(nums: list[int]) -> None:
    print(f"Original array = {nums}")
    answer = solver.moveZeroes(nums)
    print(f"Moved zeroes array = {answer}")

# Testing sortArrayByParity
def paritySortTest(nums: list[int]) -> None:
    print(f"Original array = {nums}")
    answer = solver.sortArrayByParity(nums)
    print(f"Parity array = {answer}")

# Testing pivotIndex
def pivotIndexTest(nums: list[int]) -> None:
    print(f"List = {nums}")
    answer = solver.pivotIndex(nums)
    print(f"Pivot index = {answer}")

# Testing dominantIndex
def dominantIndexTest(nums: list[int]) -> None:
    print(f"Original list = {nums}")
    answer = solver.dominantIndex(nums)
    print(f"Dominant index = {answer}")

# Testing plusOne
def plusOneTest(nums: list[int]) -> None:
    print(f"Original List = {nums}")
    answer = solver.plusOne(nums)
    print(f"Updated List = {answer}")

# Testing findDiagonalOrder - Doesn't work
# def findDiagonalOrderTest(matrix: list[list[int]]) -> None:
#     print(f"Matrix = {matrix}")
#     answer = solver.findDiagonalOrder(matrix)
#     print(f"Order = {answer}")

# Testing spiralOrder
def spiralOrderTest(matrix: list[list[int]]) -> None:
    print(f"Matrix = {matrix}")
    answer = solver.spiralOrder(matrix)
    print(f"Order = {answer}")

# Testing generate
def generatePascalTest(num: int) -> None:
    answer = solver.generate(num)
    print(f"Making a Pascal Triangle from {num} rows = {answer}")

# Testing addBinary
def binarySumTest(bin1: str, bin2: str) -> None:
    answer = solver.addBinary(bin1, bin2)
    print(f"Binary sum of {bin1} + {bin2} = {answer}")

# Testing strStr
def findStrTest(word: str, compair: str) -> None:
    print(f"Finding {compair} in {word}")
    answer = solver.strStr(word, compair)
    print(f"Index = {answer}")

# Testing longestCommonPrefix
def longestCommonPrefixTest(words: list[str]) -> None:
    answer = solver.longestCommonPrefix(words)
    print(f"Common prefix for {words} is {answer}")

# Testing reverseString
def reverseStringTest(wordStr: list[str]) -> None:
    print(f"Original word = {wordStr}")
    answer = solver.reverseString(wordStr)
    print(f"Reversed word = {answer}")

# Testing arrayPairSum
def arrayPairSumTest(nums: list[int]) -> None:
    print(f"Original list = {nums}")
    answer = solver.arrayPairSum(nums)
    print(f"The Max Sum = {answer}")

# Testing twoSum
# def twoSumTest(nums: list[int], num: int) -> None:
#     print(f"Original list = {nums}")
#     answer = solver.twoSum(nums)
#     print(f"Indecies = {answer}")
