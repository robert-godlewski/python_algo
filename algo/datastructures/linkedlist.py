# Tools Needed for Linked Lists
# For a Doubly Linked List
class ListNode:
    def __init__(self, val=None, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


# For a Doubly Linked Lists
class LL:
    def __init__(self, head=None, tail=None) -> None:
        self.head = head
        self.tail = tail
        self.size = 0
        if head and not tail:
            self.tail = head
            self.size += 1
        if tail and not head:
            self.head = tail
            self.size += 1

    def get(self, index: int):
        # Returns the value of the node at the index position (int) of the linked list
        if self.size == 0 or not self.head:
            return None
        cur = self.head
        i = 0
        while cur and i <= index:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return None

    def addAtHead(self, val: int) -> None:
        # Creates a new node with val as the stored value and is set as the new head of the linked list
        node = ListNode(val)
        if self.head:
            node.next = self.head
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        # Creates a new node with val as the stored value and set at the tail end of the linked list
        node = ListNode(val)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        if not self.head:
            self.head = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # Create a new node with val as the stored value and append it somewhere in the list based off of the index
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index < 0:
            # This will not create a new node if the index is a negative int
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

    def deleteAtIndex(self, index: int):
        # Finds the node to remove based off of it's index position and return the value of the deleted node
        if self.size == 0 or index >= self.size:
            return None
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
        return None


# Prints out the whole list from the head where head is either a ListNode or None
def printLL(head) -> str:
    listStr = "(head) -> "
    cur = head
    while cur:
        listStr += f"{cur.val} -> "
        cur = cur.next
    listStr += "(tail)"
    return listStr
