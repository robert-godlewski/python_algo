# Solutions for August 2022
# for a Singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head


class Solution:
    # Only for a Singly Linked List
    # head variable is actually a ListNode not the LinkedList class
    # O(nlog(n)) solution
    def reverseList(self, head):
        curr = head
        if curr:
            if curr.next:
                temp = self.reverseList(curr.next)
                if not temp.next:
                    curr.next = temp.next
                    temp.next = curr
                else:
                    n = temp.next
                    while n.next: n = n.next
                    curr.next = n.next
                    n.next = curr
                return temp
            else: return curr
        else: return None
