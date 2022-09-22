from hashmap_solutions202209 import Solution


solver = Solution()


print("####################")
print("Testing hashmap algorithms")


# Testing containsDuplicate
print("-----")
nums1 = [2,7,11,15]
print(f"What 2 numbers from {nums1} = 9?")
res1 = solver.twoSum(nums1,9)
print(f"Indexes are = {res1}")
print(f"9 = {nums1[res1[0]]} + {nums1[res1[1]]}")
nums2 = [3,2,4]
print(f"What 2 numbers from {nums2} = 6?")
res2 = solver.twoSum(nums2,6)
print(f"Indexes are = {res2}")
print(f"6 = {nums2[res2[0]]} + {nums2[res2[1]]}")
nums3 = [3,3]
print(f"What 2 numbers from {nums3} = 6?")
res3 = solver.twoSum(nums3,6)
print(f"Indexes are = {res3}")
print(f"6 = {nums3[res3[0]]} + {nums3[res3[1]]}")

# Testing isIsomorphic
print("-----")
print(f"Are egg and add isomorphic? {solver.isIsomorphic('egg','add')}")
print(f"Are foo and bar isomorphic? {solver.isIsomorphic('foo','bar')}")
print(f"Are paper and title isomorphic? {solver.isIsomorphic('paper','title')}")

# Testing findRestaurant
print("-----")
print("Finding common strings with the least index sum between:")
l1 = ["Shogun","Tapioca Express","Burger King","KFC"]
print(l1)
l2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(l2)
common1 = solver.findRestaurant(l1, l2)
print(f"It is {common1}")
print("Finding common strings with the least index sum between:")
l1 = ["happy","sad","good"]
print(l1)
l2 = ["sad","happy","good"]
print(l2)
common2 = solver.findRestaurant(l1, l2)
print(f"It is {common2}")
print("Finding common strings with the least index sum between:")
ls = ["k","KFC"]
print(ls)
print(ls)
common3 = solver.findRestaurant(ls,ls)
print(f"It is {common3}")

# Testing firstUniqChar
print("-----")
s1 = "leetcode"
print(f"Finding the first unique letter in: {s1}")
u1 = solver.firstUniqChar(s1)
print(f"The index = {u1}")
s2 = "loveleetcode"
print(f"Finding the first unique letter in: {s2}")
u2 = solver.firstUniqChar(s2)
print(f"The index = {u2}")
s3 = "aabb"
print(f"Finding the first unique letter in: {s3}")
u3 = solver.firstUniqChar(s3)
print(f"The index = {u3}")

# Testing intersect
print("-----")
print("Finding the intersection of:")
nums1 = [1,2,2,1]
print(nums1)
nums2 = [2,2]
print(nums2)
inter1 = solver.intersect(nums1, nums2)
print(f"Intersection are {inter1}")
print("Finding the intersection of:")
nums1 = [4,9,5]
print(nums1)
nums2 = [9,4,9,8,4]
print(nums2)
inter2 = solver.intersect(nums1, nums2)
print(f"Intersection are {inter2}")
