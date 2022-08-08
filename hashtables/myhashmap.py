# My solution on Aug 2022 - Still has runtime issues though
# Got solution from https://medium.com/analytics-vidhya/design-a-hashmap-day-1-python-8c5e463a0629 - Doesn't work, commeted out
class MyHashMap:
    def __init__(self):
        self.map_length = 10**4
        self.hash_list = [-1 for i in range(self.map_length)]

    def put(self, key, value):
        self.hash_list[key] = value
        '''
        subkey = key % self.hash_list
        if self.hash_list[subkey] == -1:
            self.hash_list[subkey] = [[key, value]]
        for i, kv in enumerate(self.hash_list[subkey]):
            if kv[0] == key: self.hash_list[subkey][i][1] = value
        '''

    def get(self, key):
        return self.hash_list[key]
        '''
        subkey = key % self.hash_list
        if self.hash_list[subkey] == -1:
            return -1
        for k, v in self.hash_list[subkey]:
            if k == key: return v
        return -1
        '''

    def remove(self, key):
        self.hash_list[key] = -1
        '''
        subkey = key % self.hash_list
        rem = -1
        for i, kv in enumerate(self.hash_list[subkey]):
            if kv[0] == key:
                rem = i
                break
        if rem != -1: del self.hash_list[subkey][rem]
        '''


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

myHashMap = MyHashMap()
myHashMap.put(1, 1) # The map is now [[1,1]]
myHashMap.put(2, 2) # The map is now [[1,1], [2,2]]
myHashMap.get(1)    # return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3)    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1) # The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2)    # return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2) # remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2)    # return -1 (i.e., not found), The map is now [[1,1]]
