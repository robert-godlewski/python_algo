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

# Trees for both levelOrder and maxDepth
# Tree 1
t1n2 = TreeNode(9)
t1n4 = TreeNode(15)
t1n5 = TreeNode(7)
t1n3 = TreeNode(20, left=t1n4, right=t1n5)
t1n1 = TreeNode(3, left=t1n2, right=t1n3)
# Tree 2
t2n1 = TreeNode(1)

# Testing levelOrder
print("-------")
nest1 = solver.levelOrder(t1n1)
print(f"The list = {nest1}")
nest2 = solver.levelOrder(t2n1)
print(f"The list = {nest2}")
nest3 = solver.levelOrder(None)
print(f"The list = {nest3}")

# Testing maxDepth
print("-------")
depth1 = solver.maxDepth(t1n1)
print(f"The depth of the tree = {depth1}")
t2n1.right = TreeNode(2)
depth2 = solver.maxDepth(t2n1)
print(f"The depth of the tree = {depth1}")
