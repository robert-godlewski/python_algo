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

# testing 
print("-------")
bin1 = solver.addBinary("11","1")
print(f"binary sum = {bin1}")
print("-------")
bin2 = solver.addBinary("1010","1011")
print(f"binary sum = {bin2}")
