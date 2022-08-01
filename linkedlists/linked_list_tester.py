from linked_list_solutions202208 import ListNode, LinkedList, Solution


solver = Solution()


print("####################")
print("Testing linked list algorithms")


def printList(ll):
    curr = ll.head
    while curr:
        print(curr.val)
        curr = curr.next


# Testing Reverse Linked List - Singly
node5 = ListNode(5)
node4 = ListNode(4, next=node5)
node3 = ListNode(3, next=node4)
node2 = ListNode(2, next=node3)
node1 = ListNode(1, next=node2)
ll1 = LinkedList(node1)
print("-----")
print("Reversing Singly Linked Lists")
print("list at start:")
printList(ll1)
ll1.head = solver.reverseList(ll1.head)
print("List reversed:")
printList(ll1)
print("empty list: []")
emptyList = LinkedList()
emptyList.head = solver.reverseList(emptyList.head)
print("empty list reversed:")
printList(emptyList)
