from binary_tree_node import TreeNode
from binary_tree_solutions import Solution


# Testing area:
solver = Solution()

node1 = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
node2 = None
node3 = TreeNode(1)
node4 = TreeNode(3, left=TreeNode(1), right=TreeNode(2))
node5 = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
node6 = TreeNode(1, right=TreeNode(2))


# For preorder
print('Preorder Traversal:')
print('=========New Root=========')
print("root = [1, None, 2, 3]")
print("Solution is:", solver.preorderTraversal(node1))
print('=========New Root=========')
print("root = []")
print("Solution is:", solver.preorderTraversal(node2))
print('=========New Root=========')
print("root = [1]")
print("Solution is:", solver.preorderTraversal(node3))
print('=========New Root=========')
print("root = [3, 1, 2]")
print("Solution is:", solver.preorderTraversal(node4))
print()

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
