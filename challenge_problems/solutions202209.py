# Basic Challenge Problem solutions in September 2022
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
class SL:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, val):
        if self.head:
            cur = self.head
            prev = None
            while cur:
                print(cur.val)
                prev = cur
                cur = cur.next
            prev.next = ListNode(val)
        else:
            self.head = ListNode(val)
        self.size += 1

    def printList(self):
        if self.head:
            cur = self.head
            while cur:
                print(cur.val)
                cur = cur.next
        else:
            print("There's nothing in this list.")
'''

class Solution:
    def runningSum(self, nums):
        # Took 10 min to solve 
        # O(n) solution
        # nums is a list of int
        # returns a list of int
        i = 1
        while i < len(nums):
            nums[i] += nums[i-1]
            i += 1
        return nums

    def maximumWealth(self, accounts) -> int:
        # Took 10 min to solve
        # O(n**2) solution
        # accounts is a nested list of int
        # returns an int
        if len(accounts) < 1 or len(accounts[0]) < 1:
            return 0
        m = len(accounts)
        n = len(accounts[0])
        i = 0
        maxsum = 0
        while i < m:
            j = 0
            subtotal = 0
            while j < n:
                subtotal += accounts[i][j]
                j += 1
            if subtotal > maxsum:
                maxsum = subtotal
            i += 1
        return maxsum

    def fizzBuzz(self, n: int):
        # Solved in 10 min
        # O(n) time
        # n is an int
        # returns a list of str
        arr = []
        i = 1
        while i <= n:
            word = ""
            add_int = True
            if i % 3 == 0:
                word += "Fizz"
                add_int = False
            if i % 5 == 0:
                word += "Buzz"
                add_int = False
            if add_int:
                word = str(i)
            arr.append(word)
            i += 1
        return arr

    def numberOfSteps(self, num: int, steps=0) -> int:
        # Solved in 5 min
        # O(log(n)) solution
        if num == 0:
            return steps
        elif num == 1:
            return steps+1
        elif num % 2 == 0:
            return self.numberOfSteps(num/2, steps+1)
        else:
            return self.numberOfSteps(num-1, steps+1)

    def middleNode(self, head):
        # Solved in 20 min
        # O(n) solution
        # head is a linked list
        # could return a linked list or nothing
        cur = head
        size = 0
        while cur:
            size += 1
            cur = cur.next
        mid = size//2
        cur = head
        i = 0
        while cur and i < mid:
            cur = cur.next
            i += 1
        return cur
