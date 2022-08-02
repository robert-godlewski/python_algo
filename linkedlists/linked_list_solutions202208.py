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

    # Only for a Singly linked List
    # Took me almost 30 min
    def removeElements(self, head, val):
        if head:
            curr = head
            prev = None
            while curr:
                if curr.val == val:
                    if curr is head:
                        head = curr.next
                        prev = curr
                        curr = curr.next
                        prev = None
                    else:
                        prev.next = curr.next
                        curr.next = None
                        curr = prev.next
                else:
                    prev = curr
                    curr = curr.next
        return head

    # Only works for Singly Linked lists
    # Took me 20 min to solve
    def isPalindrome(self, head):
        if head:
            curr = head
            arr = []
            while curr:
                arr.append(curr.val)
                curr = curr.next
            is_pal = True
            i = 0
            while i < len(arr)//2:
                if arr[i] != arr[len(arr)-1-i]:
                    is_pal = False
                    break
                i+=1
            return is_pal
        return True
