# Tools to run the tests
from datastructures.linkedlist import ListNode, LL, printLL


# Test runs
from arrays.array_tester import arrayAlgorthims


# Needed to separate algorithm groups
def thickline() -> None:
    print("============")


if __name__ == '__main__':
    thickline()
    print("Testing Array Algorithms")
    thickline()
    arrayAlgorthims()

    # Testing linked lists data structure
    thickline()
    print("Linked List Data Structures Tests")
    thickline()
    testNode = ListNode(10)
    print(f"New Node = {testNode.val}")
    llt = LL()
    print("New Linked List: " + printLL(llt.head))
    llt.addAtHead(5)
    print("Adding at the head: " + printLL(llt.head))
    llt.addAtTail(15)
    print("Adding at the tail: " + printLL(llt.head))
    llt.addAtIndex(1, 10)
    print("Adding in the middle: " + printLL(llt.head))
    #n1 = llt.get(0)
    n2 = llt.get(1)
    #n3 = llt.get(2)
    #print(f"Node 1 = {n1}")
    print(f"Node 2 = {n2}")
    #print(f"Node 3 = {n3}")
    nMid = llt.deleteAtIndex(1)
    print(f"Removed {nMid} from the linked list")
    print(printLL(llt.head))
    llt.addAtIndex(0, 1)
    print(printLL(llt.head))
    llt.deleteAtIndex(0)
    print(printLL(llt.head))
    llt.addAtIndex(2, 20)
    llt.addAtIndex(1, 10)
    print(printLL(llt.head))
    nlast = llt.deleteAtIndex(3)
    print(f"Removed {nlast} from the list")
    print(printLL(llt.head))
