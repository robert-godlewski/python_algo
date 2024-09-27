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
    # Time Complexity = O(h)
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

    # Leetcode Insert into a Binary Search Tree
    # Time Complexity = O(h)
    # Space Complexity = O(n)
    # Solved in 10 min
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val > val:
                if root.left:
                    root.left = self.insertIntoBST(root.left, val)
                else:
                    root.left = TreeNode(val)
            elif root.val < val:
                if root.right:
                    root.right = self.insertIntoBST(root.right, val)
                else:
                    root.right = TreeNode(val)
        else:
            return TreeNode(val)
        return root

    # Leetcode Delete Node in a BST - Need to study
    # Time Complexity = O(h)
    # Space Complexity = O(n)
    # Solved in 1 hr
    # Use to find a replacement
    def _popNode(self, root: TreeNode, prior: TreeNode) -> TreeNode:
        if root:
            if root.left:
                node = self._popNode(root.left, root)
            elif root.right:
                if prior.left == root:
                    prior.left = root.right
                node = root
                node.right = None
            else:
                node = None
            if node:
                return node
            else:
                if prior.left == root:
                    prior.left = None
                elif prior.right == root:
                    prior.right = None
                return root
        else:
            return None

    # Actual solution
    def deleteNode(self, root: TreeNode, key: int, is_top: bool=True, prior: TreeNode=None) -> TreeNode:
        if is_top:
            prior = None
        if root:
            if root.val > key:
                if root.left:
                    root.left = self.deleteNode(root.left, key, False, root)
            elif root.val < key:
                if root.right:
                    root.right = self.deleteNode(root.right, key, False, root)
            else:
                # root.val == key
                if root.left:
                    left = root.left
                else:
                    left = None
                if root.right:
                    right = root.right
                else:
                    right = None
                if left and right:
                    if right.left:
                        new_root = self._popNode(right.left, right)
                    else:
                        right.left = left
                        return right
                    if new_root:
                        new_root.left = left
                        new_root.right = right
                        return new_root
                elif left and not right:
                    return left
                elif right and not left:
                    return right
                else:
                    # No child node to replace
                    return None
        return root

    # Better solution to Leetcode Delete Node in a BST - Study
    def deleteNodeBetter(self, root: TreeNode, key: int) -> TreeNode:
        if root:
            if root.val < key:
                # Try and find the key in the right side
                root.right = self.deleteNodeBetter(root.right, key)
            elif root.val > key:
                # Try and find the key in the left side
                root.left = self.deleteNodeBetter(root.left, key)
            else:
                # Found the key in the BST
                if root.left and root.right:
                    node = root.right
                    while node.left:
                        node = node.left
                    root.val = node.val
                    root.right = self.deleteNodeBetter(root.right, node.val)
                elif root.left and not root.right:
                    return root.left
                elif root.right and not root.left:
                    return root.right
                else:
                    return None
        return root
