# Solutions in September 2022
class Node:
    # Only for a singly linked list
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head and self.tail:
            return False
        else:
            return True

    def enQueue(self, value):
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
        else:
            cur = self.tail
            cur.next = Node(value)
            self.tail = cur.next
    
    def deQueue(self):
        if not self.isEmpty():
            temp = self.head
            cur = temp.next
            temp.next = None
            self.head = cur
            return temp.val
        else:
            return None

    def printQueue(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next



class MyCircularQueue:
    # Took over 1 hr to implement everything here! - Still incorrect due to runtime error
    # Redid but instead of using linked lists using arrays instead - Still incorrect due to runtime error
    def __init__(self, k): 
        # k = size of the queue in int
        self.size = k
        self.data = [-1 for i in range(k)]
        self.head = -1
        self.tail = -1

    def enQueue(self, value): 
        if self.isFull():
            print("The queue is too full!")
            print(self.data)
            return False
        elif self.isEmpty():
            print(f"adding {value} to the queue: {self.data}")
            self.data[0] = value
            print(f"new queue: {self.data}")
            self.head = 0
            self.tail = 0
            return True
        else:
            print(f"adding {value} to the queue: {self.data}")
            if self.tail + 1 != self.size:
                self.tail += 1
            else:
                self.tail = 0
            self.data[self.tail] = value
            print(f"new queue: {self.data}")
            return True

    def deQueue(self): 
        if self.isEmpty():
            print("Cannot dequeue, the queue is empty!")
            return False
        else:
            print(f"current head is {self.data[self.head]} at {self.head}")
            self.data[self.head] = -1
            if self.head + 1 != self.size:
                self.head += 1
            else:
                self.head = 0
            if self.data[self.head] == -1:
                self.head = -1
                self.tail = -1
            print(f"new queue: {self.data}")
            return True

    def Front(self): 
        return self.data[self.head]

    def Rear(self):
        return self.data[self.tail]

    def isEmpty(self):
        if self.head != -1 and self.tail != -1:
            return False
        else:
            return True

    def isFull(self):
        if self.isEmpty():
            return False
        i = 0
        while i < self.size:
            if self.data[i] == -1:
                return False
            i += 1
        return True


class Solution:
    # grid is a nested list of str
    # returns an int
    # Solution in over 30 min - Still incorrect
    def numIslands(self, grid): 
        m = len(grid)
        n = len(grid[0])
        land_count = Queue()
        i = 0
        add_land = True
        while i < m:
            j = 0
            while j < n:
                if add_land:
                    if i-1 >= 0:
                        if grid[i-1][j] == "1":
                            add_land = False
                    elif j-1 >= 0:
                        if grid[i][j-1] == "1":
                            add_land = False
                if grid[i][j] == "1" and add_land:
                    land_count.enQueue(1)
                    add_land = False
                else:
                    add_land = True
                j += 1
            i += 1
        land = 0
        while not land_count.isEmpty():
            val = land_count.deQueue()
            land += val
        return land
