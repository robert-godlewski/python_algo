# Solutions to stack data structures in September 2022
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None


class Stack:
    def __init__(self) -> None:
        self.bottomNode = None
        self.topNode = None
        self.minval = None

    def printNodes(self) -> None:
        cur = self.topNode
        while cur:
            print(cur.val)
            cur = cur.next

    def push(self, val: int) -> None:
        if self.bottomNode and self.topNode:
            temp = Node(val)
            temp.next = self.topNode
            self.topNode.prev = temp
            self.topNode = temp
            if val < self.minval:
                self.minval = val
        else:
            self.bottomNode = Node(val)
            self.topNode = self.bottomNode
            self.minval = val

    def pop(self) -> None:
        if self.topNode:
            if self.topNode is self.bottomNode:
                self.bottomNode = None
                self.minval = None
            cur = self.topNode
            cur = cur.next
            if cur:
                cur.prev = None
                if self.topNode.val == self.minval:
                    self.minval = cur.val
            self.topNode.next = None
            self.topNode = cur

    def top(self) -> int:
        if self.topNode:
            return self.topNode.val
        else:
            return 0

    # Having a hard time solving this in O(1) time without getting the wrong answer
    def getMin(self) -> int: 
        if self.minval:
            return self.minval
        else:
            return 0
