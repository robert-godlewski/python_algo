# Tools needed
from algo.datastructures.tools import titleline, thinline
from algo.datastructures.linkedlist import ListNode, LL, printLL
from algo.solutions.recursion1_solutions import Solution


solver = Solution()


def recursion1Algorithms() -> None:
    titleline("Testing recursion 1 algorithms")

    reverseStringTest(["h","e","l","l","o"])
    reverseStringTest(["H","a","n","n","a","h"])
    thinline()

    ll1 = LL()
    ll1.addAtHead(1)
    ll1.addAtTail(2)
    ll1.addAtTail(3)
    ll1.addAtTail(4)
    swapPairsTest(ll1)
    #thinline()

    # Look under linked_list_tester.py for this same test
    # ll2 = LL()
    # ll2.addAtHead(1)
    # ll2.addAtTail(2)
    # ll2.addAtTail(3)
    # ll2.addAtTail(4)
    # ll2.addAtTail(5)
    # reverseLLTest(ll2)
    # ll3 = LL()
    # ll3.addAtHead(1)
    # ll3.addAtTail(2)
    # reverseLLTest(ll3)
    # reverseLLTest(None)


# Testing reverseString
def reverseStringTest(strList: list[str]) -> None:
    print(f"Original list = {strList}")
    answer = solver.reverseString(strList)
    print(f"Reversed list = {answer}")


# Testing swapPairs
def swapPairsTest(ll) -> None:
    if ll:
        print(f"Original list = {printLL(ll.head)}")
        answer = solver.swapPairs(ll.head)
    else:
        print(f"Original list = {printLL(ll)}")
        answer = solver.swapPairs(ll)
    print(f"Swapped list = {printLL(answer)}")

# Testing reverseList
def reverseLLTest(ll) -> None:
    if ll:
        print(f"Original list = {printLL(ll.head)}")
        answer = solver.reverseList(ll.head)
    else:
        print(f"Original list = {printLL(ll)}")
        answer = solver.reverseList(ll)
    print(f"Reversed list = {printLL(answer)}")
