# Solutions in September 2022
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Queue:
    def __init__(self, size=0):
        self.head = None
        self.tail = None
        # This represents the maximum size not the actual current size
        self.size = size

    def printQueue(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next


class MyCircularQueue:
    # Took over 1 hr to implement everything here! - Still incorrect due to runtime error
    def __init__(self, k): 
        # k = size of the queue in int
        self.k = k
        self.q = Queue(k)

    def enQueue(self, value): 
        if self.isEmpty():
            print(f"adding {value} to the new queue.")
            self.q.head = Node(value)
            self.q.tail = self.q.head
            print("new queue:")
            self.q.printQueue()
            return True
        elif self.isFull():
            print("The queue is too full!")
            self.q.printQueue()
            return False
        else:
            print(f"adding {value} to the queue.")
            newTail = Node(value)
            self.q.tail.next = newTail
            self.q.tail = newTail
            return True

    def deQueue(self): 
        if self.isEmpty():
            print("Cannot dequeue, the queue is empty!")
            return False
        else:
            cur = self.q.head
            cur = cur.next
            self.q.head = cur
            cur.prev = None
            print("Updated Queue:")
            self.q.printQueue()
            return True

    def Front(self): 
        if self.q.head:
            return self.q.head.val
        else:
            return -1

    def Rear(self):
        if self.q.tail:
            return self.q.tail.val
        else:
            return -1

    def isEmpty(self):
        if self.q.head and self.q.tail:
            return False
        else:
            return True

    def isFull(self):
        if self.isEmpty():
            return False
        i = 0
        cur = self.q.head
        while cur:
            i += 1
            cur = cur.next
        if i < self.k:
            return False
        else:
            return True
