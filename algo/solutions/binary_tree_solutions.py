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

    # Leetcode Binary Tree Level Order Traversal - Need to practice
    # Best Time Complexity = O(1)
    # Time Complexity = O(n)
    # Best Space Complexity = O(1)
    # Space Complexity = O(n**2)
    # Solved in 30 min
    def levelOrder(self, root: TreeNode, order: list[list[int]]=[], level: int=0) -> list[list[int]]:
        if level == 0 and len(order) > 0:
            order = []
        if root:
            if level == len(order):
                order.append([root.val])
            elif level < len(order):
                order[level].append(root.val)
            if root.left:
                order = self.levelOrder(root.left,order,level+1)
            if root.right:
                order = self.levelOrder(root.right,order,level+1)
        return order
