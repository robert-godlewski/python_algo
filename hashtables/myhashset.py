# My solution on Aug 2022 - had help from a youtube video
class MyHashSet:
    def __init__(self):
        # value range - what the question asked for but not used
        #self.set_length = 10**6
        # maximum number of operations
        self.max_opps = 10**4
        # creates a list full of empty values - Brute force way
        #self.hash_list = [None for i in range(self.set_length)]
        self.hash_list = [[] for i in range(self.max_opps)]

    def add(self, key):
        # Brute force way
        #if not self.contains(key): self.hash_list[key] = True
        subkey = key % self.max_opps
        if not self.contains(key): self.hash_list[subkey].append(key)

    def remove(self, key):
        # Brute force way
        #if self.contains(key): self.hash_list[key] = None
        subkey = key % self.max_opps
        if self.contains(key): self.hash_list[subkey].remove(key)

    def contains(self, key): 
        # Brute force way
        #return self.hash_list[key]
        subkey = key % self.max_opps
        # returns a boolean
        return key in self.hash_list[subkey]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)