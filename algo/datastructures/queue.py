# One of them is based off of a linked list
from .linkedlist import LL, printLL


class LinkedQueue(LL):
    # The head is the front of the queue
    # The tail is the back of the queue
    def __init__(self) -> None:
        super().__init__(head=None, tail=None)

    def enQueue(self, val) -> None:
        # Will only add at the back
        self.addAtTail(val)

    def deQueue(self): return self.deleteAtIndex()

    def deleteAtIndex(self):
        # Only can delete the head (aka front) of the queue
        return super().deleteAtIndex(0)

    # Making sure that the next two functions don't inherit LL functions
    def addAtHead(self, val) -> None:
        print(f"Cannot add {val} to the front of the queue")
        pass

    def addAtIndex(self, val, index: int) -> None:
        print(f"Please use enQueue function instead to add in {val}")
        print(f"With Queues only the back can be added intead of index {index}")
        pass


def printLQ(front) -> str:
    # Prints out a linked Queue
    return printLL(front, "front", "back")
