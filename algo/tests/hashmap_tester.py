# Tools needed
from algo.datastructures.tools import titleline, thinline
from algo.solutions.hashmap_solutions import Solution


solver = Solution()


# Main function to run all tests
def hashmapAlgorithms() -> None:
    titleline("Testing hashmap algorithms")

    twoSumTest([2,7,11,15],9)
    twoSumTest([3,2,4],6)
    twoSumTest([3,3],6)
    thinline()

    isIsomorphicTest('egg','add')
    isIsomorphicTest('foo','bar')
    isIsomorphicTest('paper','title')
    # thinline()

    # findRestaurantTest(["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])
    # findRestaurantTest(["happy","sad","good"],["sad","happy","good"])
    # findRestaurantTest(["k","KFC"],["k","KFC"])
    # thinline()

    # firstUniqCharTest("leetcode")
    # firstUniqCharTest("loveleetcode")
    # firstUniqCharTest("aabb")
    # thinline()

    # intersectTest([1,2,2,1],[2,2])
    # intersectTest([4,9,5],[9,4,9,8,4])


# Testing twoSum
def twoSumTest(nums: list[int], target: int) -> None:
    print(f"What 2 numbers from {nums} = {target}?")
    answer = solver.twoSum(nums,target)
    print(f"Indexes are = {answer}")
    print(f"{nums[answer[0]]} + {nums[answer[1]]} = {target}")

# Testing isIsomorphic
def isIsomorphicTest(s: str, t: str) -> None:
    answer = solver.isIsomorphic(s,t)
    print(f"Is {s} and {t} isomorphic? {answer}")

# Testing findRestaurant
def findRestaurantTest(list1: list[str], list2: list[str]) -> None:
    print("Finding common strings with the least index sum between:")
    print(list1)
    print(list2)
    answer = solver.findRestaurant(list1, list2)
    print(f"They are {answer}")

# Testing firstUniqChar
def firstUniqCharTest(s: str) -> None:
    print(f"Finding the first unique letter in {s}")
    answer = solver.firstUniqChar(s)
    print(f"The index = {answer}")
    print(f"The letter = {s[answer]}")

# Testing intersect
def intersectTest(nums1: list[int], nums2: list[int]) -> None:
    print(f"Finding the intersection of {nums1} and {nums2}")
    answer = solver.intersect(nums1, nums2)
    print(f"Intersection = {answer}")
