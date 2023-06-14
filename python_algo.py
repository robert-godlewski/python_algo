# Tools to run the tests
from datastructures.linkedlist import ListNode, LL


def thickline():
    print("============")

def thinline():
    print("------------")


if __name__ == '__main__':
    # Testing linked lists data structure
    thickline()
    print("Linked List Data Structures Tests")
    thickline()
    testNode = ListNode(10)
    print(f"New Node = {testNode.val}")
    llt = LL()
    print("New Linked List: " + llt.printLL())
    llt.addAtHead(5)
    print("Adding at the head: " + llt.printLL())
    llt.addAtTail(15)
    print("Adding at the tail: " + llt.printLL())
    llt.addAtIndex(1, 10)
    print("Adding in the middle: " + llt.printLL())
    #n1 = llt.get(0)
    n2 = llt.get(1)
    #n3 = llt.get(2)
    #print(f"Node 1 = {n1}")
    print(f"Node 2 = {n2}")
    #print(f"Node 3 = {n3}")
    nMid = llt.deleteAtIndex(1)
    print(f"Removed {nMid} from the linked list")
    print(llt.printLL())
    llt.addAtIndex(0, 1)
    print(llt.printLL())
    llt.deleteAtIndex(0)
    print(llt.printLL())
    llt.addAtIndex(2, 20)
    llt.addAtIndex(1, 10)
    print(llt.printLL())
    nlast = llt.deleteAtIndex(3)
    print(f"Removed {nlast} from the list")
    print(llt.printLL())
