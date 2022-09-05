from queue_solutions202209 import MyCircularQueue


#solver = Solution()


print("####################")
print("Testing queue algorithms")


# Testing MyCircularQueue
print("-------")
obj = MyCircularQueue(2)
print(obj.Front())
print(obj.Rear())
print(f"Is the new object empty? {obj.isEmpty()}")
val1 = 1
print(f"adding in {val1} to the queue.")
param_1 = obj.enQueue(val1)
print(f"was the addin successful? {param_1}")
print(f"is the queue empty? {obj.isEmpty()}")
print(f"is the queue full? {obj.isFull()}")
val2 = 2
print(f"adding in {val2} to the queue.")
param_2 = obj.enQueue(val2)
print(f"was the addin successful? {param_2}")
val3 = 3
print(f"adding in {val3} to the queue.")
param_3 = obj.enQueue(val3)
print(f"was the addin successful? {param_3}")
print(f"Was the queue full? {obj.isFull()}")
obj.q.printQueue()
param_4 = obj.deQueue()
print(f"removing an {obj.Front()} in the queue")
print(f"was the remove a success? {param_4}")
obj.q.printQueue()
