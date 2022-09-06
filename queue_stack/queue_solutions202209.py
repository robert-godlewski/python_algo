# Solutions in September 2022
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
    # Solution in XX - Still wrong
    def numIslands(self, grid): 
        m = len(grid)
        n = len(grid[0])
        land = 0
        i = 0
        add_land = False
        while i < m:
            j = 0
            while j < n:
                if grid[i][j] == "1":
                    if i-1 >= 0:
                        if grid[i-1][j] == "0":
                            add_land = True
                    if i+1 < m:
                        if grid[i+1][j] == "0":
                            add_land = True
                    if j-1 >= 0:
                        if grid[i][j-1] == "0":
                            add_land = True
                    if j+1 < n:
                        if grid[i][j+1] == "0":
                            add_land = True
                    if add_land:
                        land += 1
                j += 1
            i += 1
        return land
