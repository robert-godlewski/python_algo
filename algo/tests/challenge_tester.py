# Tools needed
from algo.datastructures.tools import thinline, titleline
from algo.datastructures.linkedlist import ListNode, LL, printLL
from algo.solutions.challenge_solutions import Solution


solver = Solution()


# Main function to run all tests
def challengeAlgorithms() -> None:
    titleline("Testing challenge practice algorithms")

    runSumTest([1,2,3,4])
    runSumTest([1,1,1,1,1])
    runSumTest([3,1,2,10,1])
    thinline()

    maxWealthTest([[1,2,3],[3,2,1]])
    maxWealthTest([[1,5],[7,3],[3,5]])
    maxWealthTest([[2,8,7],[7,1,3],[1,9,5]])
    thinline()

    fizzBuzzTest(3)
    fizzBuzzTest(5)
    fizzBuzzTest(15)
    thinline()

    numStepsTest(14)
    numStepsTest(8)
    numStepsTest(123)
    thinline()

    test_list = LL()
    test_list.addAtHead(1)
    test_list.addAtTail(2)
    test_list.addAtTail(3)
    test_list.addAtTail(4)
    test_list.addAtTail(5)
    findMiddleNodeTest(test_list.head)
    test_list.addAtTail(6)
    findMiddleNodeTest(test_list.head)


# Testing runningSum
def runSumTest(arr: list[int]) -> None:
    print(f"Original list = {arr}")
    answer = solver.runningSum(arr)
    print(f"Updated list = {answer}")


# Testing maximumWealth
def maxWealthTest(arr: list[list[int]]) -> None:
    print(f"Accounts = {arr}")
    answer = solver.maximumWealth(arr)
    print(f"Max = {answer}")


# testing fizzBuzz
def fizzBuzzTest(num: int) -> None:
    answer = solver.fizzBuzz(num)
    print(f"Creating a FizzBuzz array the size of {num} = {answer}")


# testing numberOfSteps
def numStepsTest(num: int) -> None:
    answer = solver.numberOfSteps(num)
    print(f"The number of steps for {num} to 0 = {answer}")


# Testing middleNode
def findMiddleNodeTest(head) -> None:
    print(f"List in = {printLL(head)}")
    answer = solver.middleNode(head)
    print(f"Middle node = {answer.val}")

