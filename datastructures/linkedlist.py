# Tools Needed for Linked Lists
class ListNode:
    def __init__(self, val=None, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


# For a linked lists
class LL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if self.size == 0:
            return 0
        cur = self.head
        i = 0
        while cur and i <= index:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return 0

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        if self.head:
            node.next = self.head
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        if not self.head:
            self.head = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index < 0:
            print("index needs to be more than 0")
        else:
            node = ListNode(val)
            cur = self.head
            prev = None
            i = 0
            while cur and i < index:
                prev = cur
                cur = cur.next
                i += 1
            prev.next = node
            node.prev = prev
            node.next = cur
            cur.prev = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> int:
        if self.size == 0 or index >= self.size:
            return 0
        # We want to delete cur
        cur = self.head
        prev = None
        i = 0
        while cur and i < index:
            prev = cur
            cur = cur.next
            i += 1
        if cur:
            ne = cur.next
            if prev:
                prev.next = ne
            if ne:
                ne.prev = prev
            if not prev:
                self.head = ne
            if not ne:
                self.tail = prev
            self.size -= 1
            return cur.val
        return 0


# Prints out the whole list from the head
def printLL(head) -> str:
    listStr = "(head) -> "
    cur = head
    while cur:
        listStr += f"{cur.val} -> "
        cur = cur.next
    listStr += "(tail)"
    return listStr
