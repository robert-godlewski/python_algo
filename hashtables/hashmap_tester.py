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
