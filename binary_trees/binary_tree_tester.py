from numpy import empty
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

# Testing isSymmetric
print("-------")
ts1n2a = TreeNode(2, TreeNode(3), TreeNode(4))
ts1n2b = TreeNode(2, TreeNode(4), TreeNode(3))
ts1n1 = TreeNode(1, ts1n2a, ts1n2b)
ts1sym = solver.isSymmetric(ts1n1)
print(f"Is the tree symmetric? {ts1sym}")

# Testing hasPathSum
print("-------")
p1n3 = TreeNode(11, left=TreeNode(7), right=TreeNode(2))
p1n2 = TreeNode(4, left=p1n3)
p1n5 = TreeNode(4, right=TreeNode(1))
p1n4 = TreeNode(8, left=TreeNode(13), right=p1n5)
p1n1 = TreeNode(5, left=p1n2, right=p1n4)
print("Is there a root-leaf sum that = 22?")
p1bool = solver.hasPathSum(p1n1, 22)
print(p1bool)
p2 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
print("Is there a root-leaf sum that = 5?")
p2bool = solver.hasPathSum(p2, 5)
print("Is there a root-leaf sum for an empty tree that = 0?")
emptyBool = solver.hasPathSum(None, 0)
print(emptyBool)
