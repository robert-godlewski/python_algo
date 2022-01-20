# LeetCode Solutions for Binary Trees
from binary_tree_node import TreeNode


class Solution:
    def preorderTraversal(self, root, data=list(), is_top=True):
        # print(type(root))
        if is_top is True and root is None: 
            # just want to return an empty list
            return list()
        elif is_top is True and root is not None: 
            # Want to clear the list for a new tree
            data = list()
        
        # Parses through the tree
        if root is not None:
            # print("Root Value:", str(root.val))
            data.append(root.val)
            # print("Data List:", data)
            # print("Root Left Node:", root.left)
            if root.left is not None: self.preorderTraversal(root.left, data, False)
            # print("Root Right Node:", root.right)
            if root.right is not None: self.preorderTraversal(root.right, data, False)
            # print("back to root")
            final_list = data
            return final_list
        else: return 0


# Testing area:
solver = Solution()

preorder_node1 = TreeNode(1)
preorder_node1.right = TreeNode(2)
preorder_node1.right.left = TreeNode(3)

preorder_node2 = None

preorder_node3 = TreeNode(1)

print("root = [1, None, 2, 3]")
print("Solution is:", solver.preorderTraversal(preorder_node1))
print("root = []")
print("Solution is:", solver.preorderTraversal(preorder_node2))
print("root = [1]")
print("Solution is:", solver.preorderTraversal(preorder_node3))
