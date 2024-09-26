# Solved in October 2024
from algo.datastructures.binary_tree import TreeNode


class Solution:
    # Leetcode Validate Binary Search Tree - Need to practice
    # Best Time Complexity = O(1)
    # Time Complexity = O(nlogn)
    # Space Complexity = O(n**2)
    # Solved in over 30 min
    # My Solution
    def isValidBST(self, root: TreeNode, stack: list[dict]=[]) -> bool:
        if root:
            if len(stack) > 0:
                i = len(stack)-1
                while i >= 0:
                    if stack[i]['going_left']:
                        if root.val >= stack[i]['value']:
                            return False
                    else:
                        if root.val <= stack[i]['value']:
                            return False
                    i -= 1
            stack.append({'value': root.val, 'going_left': True})
            if root.left:
                left_valid = self.isValidBST(root.left, stack)
            else:
                left_valid = True
            stack[len(stack)-1]['going_left'] = False
            if root.right and left_valid: #True
                right_valid = self.isValidBST(root.right, stack)
            else:
                right_valid = True
            stack.pop()
            if not left_valid or not right_valid:
                return False
        return True

    # Better solution to Leetcode Validate Binary Search Tree
    def _valid(self, node: TreeNode, left: int, right: int) -> bool:
        if not node:
            return True
        if not (left < node.val < right):
            return False
        return self._valid(node.left, left, node.val) and self._valid(node.right, node.val, right)

    def isValidBST_better(self, root: TreeNode) -> bool:
        return self._valid(root, -2**31, (2**31)-1)


    # Leetcode Search in a Binary Search Tree
    # Best Time Complexity = O(1)
    # Time Complexity = O(logn)
    # Space Complexity = O(n)
    # Solved in 10 min
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val == val:
                return root
            elif root.left and root.val > val:
                return self.searchBST(root.left, val)
            elif root.right and root.val < val:
                return self.searchBST(root.right, val)
        return None
