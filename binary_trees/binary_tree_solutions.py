# Binary Tree solutions in September 2022
from binary_tree_node import TreeNode


class Solution:
    # Solution in 30 min
    # recursively solution
    def preorderTraversal(self, root: TreeNode, nums=[], is_top=True) -> list[int]:
        if is_top and root: nums = []
        #print(f"list = {nums}")
        if root:
            #print(root.val)
            nums.append(root.val)
            if root.left:
                #print("going left:")
                nums = self.preorderTraversal(root.left, nums, False)
            if root.right:
                #print("going right:")
                nums = self.preorderTraversal(root.right, nums, False)
            #print("return to parent")
        #else: print("This is an empty tree.")
        return nums

    # Solution in 15 min
    # recursively solution
    def inorderTraversal(self, root: TreeNode, nums=[], is_top=True) -> list[int]:
        if root and is_top: nums= []
        #print(f"list = {nums}")
        if root:
            #print(root.val)
            if root.left:
                #print("going left:")
                nums = self.inorderTraversal(root.left, nums, False)
                #print("return to parent from left")
            #print(f"adding in {root.val}")
            nums.append(root.val)
            if root.right:
                #print("going right:")
                nums = self.inorderTraversal(root.right, nums, False)
                #print("return to parent from right")
        #else: print("This is an empty tree.")
        return nums

    # Solution in 7 min
    # recursively solution
    def postorderTraversal(self, root: TreeNode, nums=[], is_top=True) -> list[int]:
        if root and is_top: nums = []
        #print(f"list = {nums}")
        if root:
            #print(root.val)
            if root.left:
                #print("going left:")
                nums = self.postorderTraversal(root.left, nums, False)
                #print("return to parent from left")
            if root.right:
                #print("going right:")
                nums = self.postorderTraversal(root.right, nums, False)
                #print("return to parent from right")
            #print(f"adding in {root.val}")
            nums.append(root.val)
        #else: print("This is an empty tree.")
        return nums
