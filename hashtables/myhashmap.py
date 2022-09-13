# My solution on Aug 2022 - Still has runtime issues though
# My solution - Doesn't work in leetcode for some reason
class MyHashMap:
    def __init__(self):
        self.map_length = 10**4
        self.hash_list = [-1 for i in range(self.map_length)]

    def put(self, key, value):
        #self.hash_list[key] = value
        subkey = key % self.map_length
        self.hash_list[subkey] = value

    def get(self, key):
        #return self.hash_list[key]
        subkey = key % self.map_length
        if self.hash_list[subkey] == -1:
            return -1
        else:
            return self.hash_list[subkey]

    def remove(self, key):
        #self.hash_list[key] = -1
        subkey = key % self.map_length
        self.hash_list[subkey] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

'''
myHashMap = MyHashMap()
myHashMap.put(1, 1) # The map is now [[1,1]]
myHashMap.put(2, 2) # The map is now [[1,1], [2,2]]
myHashMap.get(1)    # return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3)    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1) # The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2)    # return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2) # remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2)    # return -1 (i.e., not found), The map is now [[1,1]]
'''
