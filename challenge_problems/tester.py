from solutions202209 import Solution


solver = Solution()


print("####################")
print("Testing challenge practice algorithms")


# Testing runningSum
print("-------")
nums1 = [1,2,3,4]
print("Original list:")
print(nums1)
print("Updated list:")
s1 = solver.runningSum(nums1)
print(s1)
print("--")
nums2 = [1,1,1,1,1]
print("Original list:")
print(nums2)
print("Updated list:")
s2 = solver.runningSum(nums2)
print(s2)
print("--")
nums3 = [3,1,2,10,1]
print("Original list:")
print(nums3)
print("Updated list:")
s3 = solver.runningSum(nums3)
print(s3)


# Testing maximumWealth
print("-------")
a1 = [[1,2,3],[3,2,1]]
print("Accounts:")
print(a1)
num1 = solver.maximumWealth(a1)
print(f"Max = {num1}")
print("--")
a2 = [[1,5],[7,3],[3,5]]
print("Accounts:")
print(a2)
num2 = solver.maximumWealth(a2)
print(f"Max = {num2}")
print("--")
a3 = [[2,8,7],[7,1,3],[1,9,5]]
print("Accounts:")
print(a3)
num3 = solver.maximumWealth(a3)
print(f"Max = {num3}")


# testing fizzBuzz
print("-------")
print("Creating a FizzBuzz array the size of 3:")
fb1 = solver.fizzBuzz(3)
print(fb1)
print("Creating a FizzBuzz array the size of 5:")
fb2 = solver.fizzBuzz(5)
print(fb2)
print("Creating a FizzBuzz array the size of 15:")
fb3 = solver.fizzBuzz(15)
print(fb3)
