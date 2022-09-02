from arr_str_solutions202209 import Solution


solver = Solution()


print("####################")
print("Testing array algorithms")


# Testing pivotIndex
nums1 = [1,7,3,6,5,6]
nums2 = [1,2,3]
nums3 = [2,1,-1]
print("-------")
piv1 = solver.pivotIndex(nums1)
print(f"Pivot index = {piv1}")
print("-------")
piv2 = solver.pivotIndex(nums2)
print(f"Pivot index = {piv2}")
print("-------")
piv3 = solver.pivotIndex(nums3)
print(f"Pivot index = {piv3}")

# Testing dominantIndex
nums1 = [3,6,1,0]
nums2 = [1,2,3,4]
print("-------")
print(f"Original list = {nums1}")
dom1 = solver.dominantIndex(nums1)
print(f"Dominant index = {dom1}")
print("-------")
print(f"Original list = {nums2}")
dom2 = solver.dominantIndex(nums2)
print(f"Dominant index = {dom2}")

# Testing plusOne
nums1 = [1,2,3]
nums2 = [4,3,2,1]
nums3 = [9]
print("-------")
dig1 = solver.plusOne(nums1)
print("-------")
dig2 = solver.plusOne(nums2)
print("-------")
dig3 = solver.plusOne(nums3)

# Testing findDiagonalOrder - Doesn't work
mat1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
mat2 = [
    [1,2],
    [3,4]
]
print("-------")
order1 = solver.findDiagonalOrder(mat1)
print(f"Order = {order1}")
print("-------")
order2 = solver.findDiagonalOrder(mat2)
print(f"Order = {order2}")

# Testing spiralOrder
mat1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
mat2 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
mat3 = [[3],[2]]
print("-------")
order1 = solver.spiralOrder(mat1)
print(f"Order = {order1}")
print("-------")
order2 = solver.spiralOrder(mat2)
print(f"Order = {order2}")
print("-------")
order3 = solver.spiralOrder(mat3)
print(f"Order = {order3}")

# Testing generate
print("-------")
pascal1 = solver.generate(5)
print("Pascal Triangle:")
print(pascal1)
print("-------")
pascal2 = solver.generate(1)
print("Pascal Triangle:")
print(pascal2)

# testing addBinary
print("-------")
bin1 = solver.addBinary("11","1")
print(f"binary sum = {bin1}")
print("-------")
bin2 = solver.addBinary("1010","1011")
print(f"binary sum = {bin2}")

# testing strStr
print("-------")
hay1 = "hello"
need1 = "ll"
print(f"finding {need1} in {hay1}")
ind1 = solver.strStr(hay1,need1)
print(f"index = {ind1}")
print("-------")
hay2 = "aaaaa"
need2 = "bba"
print(f"finding {need2} in {hay2}")
ind2 = solver.strStr(hay2,need2)
print(f"index = {ind2}")
print("-------")
hay3 = "a"
need3 = "a"
print(f"finding {need3} in {hay3}")
ind3 = solver.strStr(hay3,need3)
print(f"index = {ind3}")
# Condition where this doesn't work for some reason
print("-------")
hay4 = "abc"
need4 = "c"
print(f"finding {need4} in {hay4}")
ind4 = solver.strStr(hay4,need4)
print(f"index = {ind4}")

# testing longestCommonPrefix
print("-------")
compre1 = solver.longestCommonPrefix(["flower","flow","flight"])
print(f"common prefix = {compre1}")
print("-------")
compre2 = solver.longestCommonPrefix(["dog","racecar","car"])
print(f"common prefix = {compre2}")

# Testing reverseString
print("-------")
sin1 = ['h','e','l','l','o']
print(f"s in = {sin1}")
sout1 = solver.reverseString(sin1)
print(f"s out = {sout1}")
print("-------")
sin2 = ['H','a','n','n','a','h']
print(f"s in = {sin2}")
sout2 = solver.reverseString(sin2)
print(f"s out = {sout2}")

# Testing arrayPairSum
print("-------")
arr1 = [1,4,3,2]
print(f"arr = {arr1}")
maxsum1 = solver.arrayPairSum(arr1)
print(f"max sum = {maxsum1}")
print("-------")
arr2 = [6,2,6,5,1,2]
print(f"arr = {arr2}")
maxsum2 = solver.arrayPairSum(arr2)
print(f"max sum = {maxsum2}")

# testing twoSum
print("-------")
arr1 = [2,7,11,15]
print(f"arr = {arr1}")
ind1 = solver.twoSum(arr1,9)
print(f"indecies = {ind1}")
arr2 = [2,3,4]
print(f"arr = {arr2}")
ind2 = solver.twoSum(arr2,6)
print(f"indecies = {ind2}")
arr3 = [-1,0]
print(f"arr = {arr3}")
ind3 = solver.twoSum(arr3,-1)
print(f"indecies = {ind3}")
