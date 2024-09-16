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

    # Leetcode Maximum Depth of Binary Tree
    # Best Time Complexity = O(1)
    # Time Complexity = O(logn)
    # Best Space Complexity = O(1)
    # Space Complexity = O(n)
    # Solved in 30 min
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if root:
            left_depth = 0
            if root.left:
                left_depth = self.maxDepth(root.left)
            right_depth = 0
            if root.right:
                right_depth = self.maxDepth(root.right)
            if left_depth >= right_depth and left_depth != 0:
                depth = left_depth+1
            elif left_depth < right_depth and right_depth != 0:
                depth = right_depth+1
            else:
                # left_depth == 0 or right_depth == 0
                depth += 1
        return depth

    # Leetcode Symmetric Tree
    # Best Time Complexity = O(1)
    # Time Complexity = O(logn)
    # Best Space Complexity = O(1)
    # Space Complexity = O(n)
    # Solved in 30 min
    # Similar to the original Preorder Traversal but adds in a -200 instead
    def _leftPreorder(self, root: TreeNode, order: list[int], is_top: bool) -> list[int]:
        if is_top and len(order) > 0:
            order = []
        if root:
            order.append(root.val)
            if root.left:
                order = self._leftPreorder(root.left, order, False)
            else:
                order.append(-200)
            if root.right:
                order = self._leftPreorder(root.right, order, False)
            else:
                order.append(-200)
        return order

    # Special Preorder Traversal geared towards the right side
    def _rightPreorder(self, root: TreeNode, order: list[int], is_top: bool) -> list[int]:
        if is_top and len(order) > 0:
            order = []
        if root:
            order.append(root.val)
            if root.right:
                order = self._rightPreorder(root.right, order, False)
            else:
                order.append(-200)
            if root.left:
                order = self._rightPreorder(root.left, order, False)
            else:
                order.append(-200)
        return order

    # The Actual solution
    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            if root.left:
                left_po = self._leftPreorder(root.left, [], True)
            else:
                left_po = []
            if root.right:
                right_po = self._rightPreorder(root.right, [], True)
            else:
                right_po = []
            if left_po == right_po:
                return True
        return False

    # Leetcode Path Sum
    # Best Time Complexity = O(1)
    # Time Complexity = O(logn)
    # Best Space Complexity = O(1)
    # Space Complexity = O(n)
    # Solved in 30 min
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root:
            if root.left:
                left = self.hasPathSum(root.left,(targetSum-root.val))
            else:
                left = False
            if left:
                return True
            if root.right:
                right = self.hasPathSum(root.right,(targetSum-root.val))
            else:
                right = False
            if right:
                return True
            if root.val == targetSum and not root.left and not root.right:
                return True
        return False
