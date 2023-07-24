# One of them is based off of a linked list
from .linkedlist import LL, printLL


class LinkedStack(LL):
    # The top is the tail of the stack
    # The bottom is the head of the stack
    def __init__(self) -> None:
        super().__init__(head=None, tail=None)

    def push(self, val) -> None:
        # Will only add at the top
        self.addAtTail(val)

    def pop(self): return self.deleteAtIndex()

    def deleteAtIndex(self):
        # Only can delete the tail (aka top) of the stack
        return super().deleteAtIndex(self.size-1)

    # Making sure that the next two functions don't inherit LL functions
    def addAtHead(self, val) -> None:
        print(f"Cannot add {val} to the bottom of the stack")
        pass

    def addAtIndex(self, val, index: int) -> None:
        print(f"Please use push function instead to add in {val}")
        print(f"With Stacks only the top can be added instead of index {index}")
        pass


def printLS(bottom) -> str:
    # Prints out a linked Queue
    return printLL(bottom, "bottom", "top")