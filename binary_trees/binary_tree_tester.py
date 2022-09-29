from binary_tree_node import TreeNode
from binary_tree_solutions import Solution


# Testing area:
solver = Solution()


print("####################")
print("Testing binary tree algorithms")

# Testing preorderTraversal
print("-------")
t1n3 = TreeNode(3)
t1n2 = TreeNode(2, left=t1n3)
t1n1 = TreeNode(1, right=t1n2)
arr1 = solver.preorderTraversal(t1n1)
print(f"The list = {arr1}")
arr2 = solver.preorderTraversal(None)
print(f"The list = {arr2}")
t3n1 = TreeNode(1)
arr3 = solver.preorderTraversal(t3n1)
print(f"The list = {arr3}")

# Testing inorderTraversal
print("-------")
t1n3 = TreeNode(3)
t1n2 = TreeNode(2, left=t1n3)
t1n1 = TreeNode(1, right=t1n2)
arr1 = solver.inorderTraversal(t1n1)
print(f"The list = {arr1}")
arr2 = solver.inorderTraversal(None)
print(f"The list = {arr2}")
t3n1 = TreeNode(1)
arr3 = solver.inorderTraversal(t3n1)
print(f"The list = {arr3}")

# Testing postorderTraversal
print("-------")
t1n3 = TreeNode(3)
t1n2 = TreeNode(2, left=t1n3)
t1n1 = TreeNode(1, right=t1n2)
arr1 = solver.postorderTraversal(t1n1)
print(f"The list = {arr1}")
arr2 = solver.postorderTraversal(None)
print(f"The list = {arr2}")
t3n1 = TreeNode(1)
arr3 = solver.postorderTraversal(t3n1)
print(f"The list = {arr3}")

# Testing levelOrder
print("-------")
t1n2 = TreeNode(9)
t1n4 = TreeNode(15)
t1n5 = TreeNode(7)
t1n3 = TreeNode(20, left=t1n4, right=t1n5)
t1n1 = TreeNode(3, left=t1n2, right=t1n3)
nest1 = solver.levelOrder(t1n1)
print(f"The list = {nest1}")
t2n1 = TreeNode(1)
nest2 = solver.levelOrder(t2n1)
print(f"The list = {nest2}")
nest3 = solver.levelOrder(None)
print(f"The list = {nest3}")

# old stuff
'''
# For solving the depth of the tree
print('Maximum Depth finder:')
print("Solution for root = [3,9,20,null,null,15,7] is:")
print(str(solver.maxDepth(node5)))
print("Solution for root = [1,null,2] is:")
print(str(solver.maxDepth(node6)))
'''
