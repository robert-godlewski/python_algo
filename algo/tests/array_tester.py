# Tools needed
from algo.datastructures.tools import titleline, thinline
from algo.solutions.array_solutions import Solution


solver = Solution()


# Main function to run all tests
def arrayAlgorthims() -> None:
    titleline("Testing Array Algorithms")

    # This is in the easy collection of top interview questions
    removeDuplicatesTest([1,1,2])
    removeDuplicatesTest([0,0,1,1,1,2,2,3,3,4])
    thinline()

    # This is in the easy collection of top interview questions
    maxProfitTest([7,1,5,3,6,4])
    maxProfitTest([1,2,3,4,5])
    maxProfitTest([7,6,4,3,1])
    maxProfitTest([2,1,2,0,1])
    thinline()

    # This is in the easy collection of top interview questions
    rotateArrTest([1,2,3,4,5,6,7],3)
    rotateArrTest([-1,-100,3,99],2)
    thinline()

    # This is in the easy collection of top interview questions
    duplicateTest([1,2,3,1])
    duplicateTest([1,2,3,4])
    duplicateTest([1,1,1,3,3,4,3,2,4,2])
    thinline()

    # This is in the easy collection of top interview questions
    singleNumTest([2,2,1])
    singleNumTest([4,1,2,1,2])
    singleNumTest([1])
    thinline()

    # This is in the easy collection of top interview questions
    intersectTest2([1,2,2,1],[2,2])
    intersectTest2([4,9,5],[9,4,9,8,4])
    thinline()

    # This is in the easy collection of top interview questions
    plusOneTest([1,2,3])
    plusOneTest([4,3,2,1])
    plusOneTest([9])
    thinline()

    # This is in the easy collection of top interview questions
    moveZeroesTest([0,1,0,3,12])
    moveZeroesTest([0])
    thinline()

    # This is in the easy collection of top interview questions
    twoSumTest([2,7,11,15],9)
    twoSumTest([3,2,4],6)
    twoSumTest([3,3],6)
    twoSumTest([-1,0],-1)
    thinline()

    # This is in the easy collection of top interview questions
    validSudokuTest([
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ])
    validSudokuTest([
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ])
    thinline()

    # This is in the easy collection of top interview questions - Still need to fix
    rotateImageTest([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])
    rotateImageTest([
        [5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15,14,12,16]
    ])

    # duplicateZerosTest([1,0,2,3,0,4,5,0])
    # duplicateZerosTest([1,2,3])
    # thinline()

    # mergeArrTest([1,2,3,0,0,0], 3, [2,5,6], 3)
    # mergeArrTest([1], 1, [], 0)
    # mergeArrTest([0], 0, [1], 1)
    # mergeArrTest([4,5,6,0,0,0], 3, [1,2,3], 3)
    # mergeArrTest([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3)
    # thinline()

    # removeElementTest([3,2,2,3], 3)
    # removeElementTest([0,1,2,2,3,0,4,2], 2)
    # thinline()

    # mountArrTest([2,1])
    # mountArrTest([3,5,5])
    # mountArrTest([0,3,2,1])
    # mountArrTest([2])
    # mountArrTest([0,1,2,3])
    # thinline()

    # replaceETests([17,18,5,4,6,1])
    # replaceETests([400])
    # thinline()

    # paritySortTest([3,1,2,4])
    # paritySortTest([0])
    # thinline()

    # heightCheckerTest([1,1,4,2,1,3])
    # heightCheckerTest([5,1,2,3,4])
    # heightCheckerTest([1,2,3,4,5])
    # thinline()

    # pivotIndexTest([1,7,3,6,5,6])
    # pivotIndexTest([1,2,3])
    # pivotIndexTest([2,1,-1])
    # thinline()

    # dominantIndexTest([3,6,1,0])
    # dominantIndexTest([1,2,3,4])
    # dominantIndexTest([1,0])
    # thinline()

    # findDiagonalOrderTest([[1,2,3],[4,5,6],[7,8,9]])
    # findDiagonalOrderTest([[1,2],[3,4]])
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

    # arrayPairSumTest([1,4,3,2])
    # arrayPairSumTest([6,2,6,5,1,2])
    # thinline()


# Testing removeDuplicates
def removeDuplicatesTest(arr: list[int]) -> None:
    print(f"Removing duplicates in {arr}")
    remain = solver.removeDuplicates(arr)
    print(f"Number of values taken out = {remain}")

# Testing maxProfit
def maxProfitTest(nums: list[int]) -> None:
    print(f"Prices per day = {nums}")
    answer = solver.maxProfit(nums)
    print(f"The maximum profit would be = {answer}")

# Testing rotate
def rotateArrTest(nums: list[int], k: int) -> None:
    # nums = the array we are using
    # k = the number of steps to rotate
    print(f"Array before rotation = {nums}")
    print(f"Rotating array by {k} steps")
    answer = solver.rotate(nums, k)
    print(f"Rotated array = {answer}")

# Testing containsDuplicate
def duplicateTest(nums: list[int]) -> None:
    print(f"Does this array have duplicates? {nums}")
    answer = solver.containsDuplicate(nums)
    print(answer)

# Testing singleNumber
def singleNumTest(nums: list[int]) -> None:
    print(f"What is the single number this array? {nums}")
    answer = solver.singleNumber(nums)
    print(answer)

# Testing intersect (Intersection of 2 Arrays 2)
def intersectTest2(nums1: list[int], nums2: list[int]) -> None:
    print(f"What is the intersection of {nums1} and {nums2}?")
    answer = solver.intersect(nums1,nums2)
    print(answer)

# Testing plusOne
def plusOneTest(nums: list[int]) -> None:
    print(f"Original List = {nums}")
    answer = solver.plusOne(nums)
    print(f"Updated List = {answer}")

# Testing moveZeroes
def moveZeroesTest(nums: list[int]) -> None:
    print(f"Original array = {nums}")
    answer = solver.moveZeroes(nums)
    print(f"Moved zeroes array = {answer}")

# Testing twoSum
def twoSumTest(nums: list[int], num: int) -> None:
    print(f"Original list = {nums}")
    print(f"Target = {num}")
    answer = solver.twoSum(nums, num)
    print(f"Indecies = {answer}")
    print(f"{num} = nums[{answer[0]}] + nums[{answer[1]}] = {nums[answer[0]]} + {nums[answer[1]]}")

# Testing isValidSudoku
def validSudokuTest(board: list[list[str]]) -> None:
    print("Is this board valid? [")
    for row in board:
        print(row)
    print("]")
    answer = solver.isValidSudoku(board)
    if answer:
        print("The board is valid")
    else:
        print("The board is not valid")

# Testing rotate
def rotateImageTest(matrix: list[list[int]]) -> None:
    print("Rotating this matrix: [")
    for row in matrix:
        print(row)
    print("]")
    answer = solver.rotateImg(matrix)
    print("To: [")
    for row in answer:
        print(row)
    print("]")

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

# Testing sortArrayByParity
def paritySortTest(nums: list[int]) -> None:
    print(f"Original array = {nums}")
    answer = solver.sortArrayByParity(nums)
    print(f"Parity array = {answer}")

# Testing heightChecker
def heightCheckerTest(heights: list[int]) -> None:
    print(f"Original array = {heights}")
    answer = solver.heightChecker(heights)
    if answer == 0:
        print("All height indices match with what's expected")
    else:
        print(f"There are {answer} indices where the indices do not match for what's expected")

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

# Testing findDiagonalOrder
def findDiagonalOrderTest(matrix: list[list[int]]) -> None:
    print(f"Matrix = {matrix}")
    answer = solver.findDiagonalOrder(matrix)
    print(f"Order = {answer}")

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

# Testing arrayPairSum
def arrayPairSumTest(nums: list[int]) -> None:
    print(f"Original list = {nums}")
    answer = solver.arrayPairSum(nums)
    print(f"The Max Sum = {answer}")
