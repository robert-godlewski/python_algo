# Solved in October 2024
from algo.datastructures.binary_tree import TreeNode


class Solution:
    # Leetcode Validate Binary Search Tree - Need to practice/ doesn't work
    # Time Complexity
    # Space Complexity
    # Solved in over 30 min
    '''
    bst4 - Not Working
    '''
    def isValidBST(self, root: TreeNode) -> bool:
        if root:
            if root.left:
                left_valid = self.isValidBST(root.left)
                if left_valid:
                    if root.val <= root.left.val:
                        return False
                else:
                    return False
            if root.right:
                right_valid = self.isValidBST(root.right)
                if right_valid:
                    if root.val >= root.right.val:
                        return False
                else:
                    return False
        return True