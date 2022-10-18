# Binary Tree solutions in September and October 2022
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

    # Solved in 20 minutes - bad solution
    # Used for the left side
    def preorderTraversalLeft(self, root: TreeNode, nums=[], is_top=True) -> list:
        if is_top and root: nums = []
        if root:
            nums.append(root.val)
            if root.left:
                nums = self.preorderTraversalLeft(root.left, nums, False)
            else:
                nums.append("None")
            if root.right:
                nums = self.preorderTraversalLeft(root.right, nums, False)
            else:
                nums.append("None")
        return nums

    # Used for the right side
    # Similar to a preorder traversal but favors the right side before left side
    def preorderTraversalRight(self, root: TreeNode, nums=[], is_top=True) -> list:
        if is_top and root: nums = []
        if root:
            nums.append(root.val)
            if root.right: 
                nums = self.preorderTraversalRight(root.right, nums, False)
            else:
                nums.append("None")
            if root.left:
                nums = self.preorderTraversalRight(root.left, nums, False)
            else:
                nums.append("None")
        return nums

    # Main solution
    def isSymmetric(self, root: TreeNode) -> bool:
        if root.left and root.right:
            # First traverse the left side and add to a queue
            lqueue = self.preorderTraversal(root.left)
            rqueue = self.preorderTraversalRight(root.right)
            if lqueue == rqueue:
                return True
            else:
                return False
        elif root.left or root.right:
            return False
        else:
            return True

    # Solved in 30 min
    def hasPathSum(self, root: TreeNode, targetSum: int, is_top=True, temp_sum=0) -> bool:
        if root:
            if is_top:
                temp_sum = 0
            #print(f"Current value = {root.val}")
            temp_sum += root.val
            #print(f"Current sum = {temp_sum}")
            if temp_sum == targetSum and not root.left and not root.right:
                return True
            l_found = False
            if root.left:
                #print("Checking left side")
                l_found = self.hasPathSum(root.left, targetSum, False, temp_sum)
                #print("returning to parent")
            #else: print("No left side")
            if l_found:
                return True
            r_found = False
            if root.right:
                #print("checking right side")
                r_found = self.hasPathSum(root.right, targetSum, False, temp_sum)
                #print("returning to parent")
            #else: print("No right side")
            if r_found:
                return True
        return False
