# My solution on Aug 2022 - had help from a youtube video
class MyHashSet:
    def __init__(self, length=10**6):
        # length is the maximum lenght of the set
        # maximum number of operations - needed for leetcode specific solution
        #self.max_opps = 10**4
        # creates a list full of empty values - Brute force way
        #self.hash_list = [None for i in range(self.set_length)]
        self.length = length
        self.hash_list = [[] for i in range(self.length)]

    def add(self, key):
        # Brute force way
        #if not self.contains(key): self.hash_list[key] = True
        subkey = key % self.length
        if not self.contains(key): self.hash_list[subkey].append(key)

    def remove(self, key):
        # Brute force way
        #if self.contains(key): self.hash_list[key] = None
        subkey = key % self.length
        if self.contains(key): self.hash_list[subkey].remove(key)

    def contains(self, key): 
        # Brute force way
        #return self.hash_list[key]
        subkey = key % self.length
        return key in self.hash_list[subkey]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)