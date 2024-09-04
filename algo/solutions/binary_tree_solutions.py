# Binary Tree solutions in September 2024
from algo.datastructures.binary_tree import TreeNode


class Solution:
    # Leetcode Binary Tree Preorder Traversal
    # Time Complexity = O(1)
    # Space Complexity = O(n)
    # Solved in 5 min
    def preorderTraversal(self, root: TreeNode, order: list[int]=[], is_top: bool=True) -> list[int]:
        if is_top:
            order = []
        if root:
            order.append(root.val)
            if root.left:
                order = self.preorderTraversal(root.left, order, False)
            if root.right:
                order = self.preorderTraversal(root.right, order, False)
        return order

    # Leetcode Binary Tree Inorder Traversal
    # Time Complexity = O(1)
    # Space Complexity = O(n)
    # Solved in 5 min
    def inorderTraversal(self, root: TreeNode, order: list[int]=[], is_top: bool=True) -> list[int]:
        if is_top:
            order = []
        if root:
            if root.left:
                order = self.inorderTraversal(root.left, order, False)
            order.append(root.val)
            if root.right:
                order = self.inorderTraversal(root.right, order, False)
        return order

    # Leetcode Binary Tree Postorder Traversal
    # Time Complexity = O(1)
    # Space Complexity = O(n)
    # Solved in 5 min
    def postorderTraversal(self, root: TreeNode, order: list[int]=[], is_top: bool=True) -> list[int]:
        if is_top:
            order = []
        if root:
            if root.left:
                order = self.postorderTraversal(root.left, order, False)
            if root.right:
                order = self.postorderTraversal(root.right, order, False)
            order.append(root.val)
        return order
