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


# Testing removeElements
node6a = ListNode(6)
node5 = ListNode(5, node6a)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node6b = ListNode(6, node3)
node2 = ListNode(2, node6b)
node1 = ListNode(1, node2)
ll2 = LinkedList(node1)
print("-----")
print("Removing elements from a Linked List")
print("list at start:")
printList(ll2)
ll2.head = solver.removeElements(ll2.head, 6)
print("Updated list:")
printList(ll2)
'''
Infinate loop in the test but ok in leetcode
node7 = ListNode(7)
ll7s = LinkedList(node7)
ll7s.head.next = node7
ll7s.head.next.next = node7
ll7s.head.next.next.next = node7
print(" List of 7s at start:")
printList(ll7s)
ll7s.head = solver.removeElements(ll7s.head, 7)
print("Updated list with removal of 7s:")
printList(ll7s)
'''


# Testing isPalindrome
node1a = ListNode(1)
node2a = ListNode(2, node1a)
node2b = ListNode(2, node2a)
node1b = ListNode(1, node2b)
llpalidrome = LinkedList(node1b)
print("-----")
print("checking to see if this is a palidrome or not")
print("List:")
printList(llpalidrome)
is_pali = solver.isPalindrome(llpalidrome.head)
print(f"List is palidrome? {is_pali}")
print("List:")
printList(ll1)
is_not_pal = solver.isPalindrome(ll1.head)
print(f"List is palidrome? {is_not_pal}")
