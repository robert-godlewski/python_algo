# Recursion 1 solutions in September 2022
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class SLL:
    def __init__(self) -> None:
        self.head = None

    def printSLL(self) -> None:
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next


class Solution:
    # Solved in less than 10 min
    # O(n) Time solution
    def reverseString(self, s: list) -> list:
        # Do not return anything, modify s in-place instead. - In leetcode, return None
        # Natively return a list of str
        # s is a list of str
        length = len(s)//2
        i = 0
        while i < length:
            temp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = temp
            i += 1
            print(s)
        # Don't add this part to leetcode
        return s

    # Solved in 40 min
    # Wrong in LeetCode, not too sure how to get it to work but works localy
    def swapPairs(self, head: ListNode, is_swaping=True, prev=None) -> None:
        print(head.val)
        if head.next:
            if is_swaping:
                temp = head
                head = head.next
                temp.next = head.next
                head.next = temp
                if prev:
                    prev.next = head
                is_swaping = False
            else:
                is_swaping = True
            self.swapPairs(head=head.next, is_swaping=is_swaping, prev=head)
