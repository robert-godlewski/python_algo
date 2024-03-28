# Tools needed
from algo.datastructures.tools import titleline, thinline
from algo.solutions.string_solutions import Solution


solver = Solution()


# Main function to run all tests
def stringAlgorithms() -> None:
    titleline("Testing String Algorithms")

    # This is in the easy collection of top interview questions
    reverseStringTest(['h','e','l','l','o'])
    reverseStringTest(['H','a','n','n','a','h'])
    thinline()

    # This is in the easy collection of top interview questions
    reverseIntTest(123)
    reverseIntTest(-123)
    reverseIntTest(120)
    reverseIntTest(1534236469)
    thinline()

    # This is in the easy collection of top interview questions
    firstUniqCharTest("leetcode")
    firstUniqCharTest("loveleetcode")
    firstUniqCharTest("aabb")

    # Will need these later, were part of array_tester.py
    # findStrTest("sadbutsad", "sad")
    # findStrTest("leetcode", "leeto")
    # findStrTest("hello", "ll")
    # findStrTest("aaaaa", "bba")
    # findStrTest("a", "a")
    # findStrTest("abc", "c")
    # findStrTest("mississippi", "issip")
    # findStrTest("mississippi", "pi")
    # thinline()

    # longestCommonPrefixTest(["flower","flow","flight"])
    # longestCommonPrefixTest(["dog","racecar","car"])
    # longestCommonPrefixTest(["cir","car"])
    # thinline()


# Testing reverseString
def reverseStringTest(wordStr: list[str]) -> None:
    print(f"Original word = {wordStr}")
    answer = solver.reverseString(wordStr)
    print(f"Reversed word = {answer}")

# Testing reverseInt
def reverseIntTest(x: int) -> None:
    print(f"Original number = {x}")
    answer = solver.reverseInt(x)
    print(f"Reversed number = {answer}")

# Testing firstUniqChar
def firstUniqCharTest(s: str) -> None:
    print(f"String = {s}")
    answer = solver.firstUniqChar(s)
    print(f"Index of the unique character = {answer}")
    print(f"The unique character is = {s[answer]}")

# Will need to test and solve later for those below
# Testing strStr
def findStrTest(word: str, compair: str) -> None:
    print(f"Finding {compair} in {word}")
    answer = solver.strStr(word, compair)
    print(f"Index = {answer}")

# Testing longestCommonPrefix
def longestCommonPrefixTest(words: list[str]) -> None:
    answer = solver.longestCommonPrefix(words)
    print(f"Common prefix for {words} is {answer}")
