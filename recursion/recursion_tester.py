from recursion_solutions202210 import Solution, ListNode, SLL


solver = Solution()


print("####################")
print("Testing recursion 1 algorithms")

# Testing reverseString
print("-------")
s1 = ["h","e","l","l","o"]
print(f"Reversing: {s1}")
reverse1 = solver.reverseString(s1)
print(f"Reversed = {reverse1}")
s2 = ["H","a","n","n","a","h"]
print(f"Reversing: {s2}")
reverse2 = solver.reverseString(s2)
print(f"Reversed = {reverse2}")

# Testing swapPairs
print("-------")
n4 = ListNode(val=4)
n3 = ListNode(val=3, next=n4)
n2 = ListNode(val=2, next=n3)
n1 = ListNode(val=1, next=n2)
l1 = SLL()
l1.head = n1
print("Original list:")
l1.printSLL()
solver.swapPairs(l1.head)
l1.head = n2
print("New List:")
l1.printSLL()
