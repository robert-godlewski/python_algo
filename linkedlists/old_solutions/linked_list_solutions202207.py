# Solutions solved in July 2022
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# For linked lists - For some reason Leetcode doesn't like this build for some reason
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # returns the value at the given index
    def get(self, index):
        if not self.head or index > self.size or index < 0: return -1
        current_node = self.head
        i = 0
        while current_node and i < self.size:
            if i == index:
                return current_node.val
            else:
                current_node = current_node.next
                i += 1

    def addAtHead(self, val):
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        self.size += 1

    def addAtTail(self, val):
        current_node = self.head
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.size += 1

    def addAtIndex(self, index, val):
        if index <= 0:
            self.addAtHead(val)
        elif index == self.size-1:
            self.addAtTail(val)
        elif index < self.size:
            current_node = self.head
            i = 0
            while current_node is not None and i < index:
                current_node = current_node.next
                i += 1
            temp = current_node.next
            current_node.next = Node(val)
            current_node = current_node.next
            current_node.next = temp
            self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size: return
        current_node = self.head
        if index == 0: self.head = current_node.next
        else:
            i = 0
            while current_node.next is not None and i < index-1:
                current_node = current_node.next
                i += 1
            if current_node.next is not None:
                del_node = current_node.next
                if del_node.next is not None:
                    current_node.next = del_node.next
                    del_node.next = None
            else:
                current_node.next = None
        self.size -= 1


class Solution: pass