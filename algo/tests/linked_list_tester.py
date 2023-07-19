# Tools needed
from algo.datastructures.tools import titleline, thinline
from algo.datastructures.linkedlist import LL, printLL
from algo.solutions.linked_list_solutions import Solution


solver = Solution()


# Main function to run all tests
def linkedlistAlgorithms() -> None:
    titleline("Testing linked list algorithms")

    ll1 = LL()
    ll1.addAtTail(1)
    ll1.addAtTail(2)
    ll1.addAtTail(3)
    ll1.addAtTail(4)
    ll1.addAtTail(5)
    reverseLLTest(ll1)
    reverseLLTest(None)
    thinline()

    ll2 = LL()
    ll2.addAtTail(1)
    ll2.addAtTail(2)
    ll2.addAtTail(6)
    ll2.addAtTail(3)
    ll2.addAtTail(4)
    ll2.addAtTail(5)
    ll2.addAtTail(6)
    removeElementsTest(ll2, 6)
    # Might cause an infiniate loop but in leetcode it's ok
    sevens = LL()
    sevens.addAtHead(7)
    sevens.addAtHead(7)
    sevens.addAtHead(7)
    sevens.addAtHead(7)
    removeElementsTest(sevens, 7)
    thinline()

    ll3 = LL()
    ll3.addAtHead(1)
    ll3.addAtTail(2)
    ll3.addAtTail(2)
    ll3.addAtTail(1)
    palindromeListTest(ll3)
    palindromeListTest(ll1)


# Testing Reverse Linked List - Singly
def reverseLLTest(ll) -> None:
    if ll:
        print(f"Original list = {printLL(ll.head)}")
        answer = solver.reverseList(ll.head)
    else:
        print(f"Original list = {printLL(ll)}")
        answer = solver.reverseList(ll)
    print(f"Reversed list = {printLL(answer)}")


# Testing removeElements
def removeElementsTest(ll, val) -> None:
    print(f"Value removing from the list = {val}")
    if ll:
        print(f"Original list = {printLL(ll.head)}")
        answer = solver.removeElements(ll.head, val)
    else:
        print("Original list = none")
        answer = solver.removeElements(ll, val)
    print(f"Updated list = {printLL(answer)}")


# Testing isPalindrome
def palindromeListTest(ll) -> None:
    if ll:
        print(f"List = {printLL(ll.head)}")
        answer = solver.isPalindrome(ll.head)
    else:
        print(f"List = {printLL(ll)}")
        answer = solver.isPalindrome(ll)
    print(f"Is this list a palindrome? {answer}")
