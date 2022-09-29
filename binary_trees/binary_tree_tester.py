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


# old stuff
'''
node1 = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
node2 = None
node3 = TreeNode(1)
node4 = TreeNode(3, left=TreeNode(1), right=TreeNode(2))
node5 = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
node6 = TreeNode(1, right=TreeNode(2))


# For inorder
print('Inorder Traversal:')
print('=========New Root=========')
print("root = [1, None, 2, 3]")
print("Solution is:", solver.inorderTraversal(node1))
print('=========New Root=========')
print("root = []")
print("Solution is:", solver.inorderTraversal(node2))
print('=========New Root=========')
print("root = [1]")
print("Solution is:", solver.inorderTraversal(node3))
print('=========New Root=========')
print("root = [3, 1, 2]")
print("Solution is:", solver.inorderTraversal(node4))
print()

# For postorder
print('Postorder Traversal:')
print('=========New Root=========')
print("root = [1, None, 2, 3]")
print("Solution is:", solver.postorderTraversal(node1))
print('=========New Root=========')
print("root = []")
print("Solution is:", solver.postorderTraversal(node2))
print('=========New Root=========')
print("root = [1]")
print("Solution is:", solver.postorderTraversal(node3))
print('=========New Root=========')
print("root = [3, 1, 2]")
print("Solution is:", solver.postorderTraversal(node4))
print()

# For levelorder
print('Level Order Traversal:')
print("Solution for root = [3,9,20,null,null,15,7] is:")
print(str(solver.levelOrder(node5)))
print("Solution for root = [1] is:")
print(str(solver.levelOrder(node3)))
print("Solution for root = [] is:")
print(str(solver.levelOrder(node2)))
print()

# For solving the depth of the tree
print('Maximum Depth finder:')
print("Solution for root = [3,9,20,null,null,15,7] is:")
print(str(solver.maxDepth(node5)))
print("Solution for root = [1,null,2] is:")
print(str(solver.maxDepth(node6)))
'''
