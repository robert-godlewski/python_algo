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

    # Solution in over 1 hr
    def levelOrder(self, root: TreeNode, nest=[], level=0) -> list[list[int]]:
        # clearing the nest list
        if root and level == 0:
            nest = []
        # Checking if there is a root
        if root:
            #print(f"current level of the tree = {level}")
            #print(root.val)
            # Testing to see if there is a list within nest at index level, if not it will add a list at the end
            try:
                nest[level].append(1)
                nest[level].pop()
            except:
                nest.append([])
            # adding the root value to the list at the proper level index
            nest[level].append(root.val)
            #print(f"Current nested list = {nest}")
            # checking to see if there is a left child node
            if root.left:
                #print(f"going left, level {level+1}")
                nest = self.levelOrder(root.left, nest, level+1)
                #print(f"returning to level {level}")
            # Checking to see if there is a right child node
            if root.right:
                #print(f"going right, level {level+1}")
                nest = self.levelOrder(root.right, nest, level+1)
                #print(f"returning to level {level}")
        return nest

    # Solved over 1 hr
    def maxDepth(self, root: TreeNode, depth=1, curDepth=1) -> int:
        if root:
            #print(f"Current depth = {curDepth}")
            #print(f"Currently on node {root.val} in the tree")
            # update the depth for each level
            if curDepth > depth:
                depth += 1
            # check the left side and update the depth
            if root.left:
                #print("Checking left")
                depth = self.maxDepth(root.left, depth, curDepth+1)
                #print("returning to parent")
            # Check the right side and update the depth
            if root.right:
                #print("Checking right")
                depth = self.maxDepth(root.right, depth, curDepth+1)
                #print("returning to parent")
            #print(f"depth returning = {depth}")
        else:
            # If there isn't a root return 0
            return 0
        return depth
