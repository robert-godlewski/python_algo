# LeetCode Solutions for Binary Trees
from binary_tree_node import TreeNode


class Solution:
    # Iterative solution
    def preorderTraversalIterative(self, root):
        # print(type(root))
        if root is None: return list()
        data = [root]
        # print(f"Data processing: {data}")
        answer = list()
        while len(data) > 0: 
            node = data.pop()
            # print("Current Node in Review:", node)
            if node is not None:
                # print("Current Node value:", node.val)
                answer.append(node.val)
                if node.right is not None: 
                    # print("Right Node:", node.right.val)
                    data.append(node.right)
                if node.left is not None: 
                    # print("Left Node:", node.left.val)
                    data.append(node.left)
            # print('Current Answer:', answer)
            # print('Length of Data list:', len(data))
            # print('==================')
        return answer
    
    # Recursive way - Regular way
    def preorderTraversalSlow(self, root, data=list(), is_top=True):
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

    # Recursive way - Super slick way
    def preorderTraversal(self, root):
        if root:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        else: return list()

    # Recursive way - Regular way
    def inorderTraversalSlow(self, root, data=list(), is_top=True):
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
            if root.left is not None: 
                # print("Root Left Node:", root.left)
                self.inorderTraversal(root.left, data, False)
            data.append(root.val)
            if root.right is not None: 
                # print("Root Right Node:", root.right)
                self.inorderTraversal(root.right, data, False)
            # print("Data List:", data)
            # print("back to root")
            final_list = data
            return final_list
        else: return 0

    # Recursive way - Super slick way
    def inorderTraversal(self, root):
        if root:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        else: return list()

    # Recursive way - Regular way
    def postorderTraversalSlow(self, root, data=list(), is_top=True):
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
            if root.left is not None: 
                # print("Root Left Node:", root.left)
                self.postorderTraversal(root.left, data, False)
            if root.right is not None: 
                # print("Root Right Node:", root.right)
                self.postorderTraversal(root.right, data, False)
            data.append(root.val)
            # print("Data List:", data)
            # print("back to root")
            final_list = data
            return final_list
        else: return 0

    # Recursive way - Super slick way
    def postorderTraversal(self, root):
        if root:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        else: return list()

    # Recursive way
    def levelOrder(self, root, data=list(), level=0):
        # print('=====================')
        if level == 0 and root is None:
            # just want to return an empty list
            return list()
        elif level == 0 and root is not None:
            # Want to clear the list for a new tree
            data = list()
        
        try: 
            # print(f"Has an index: {data[level]}")
            data[level].append(1)
            data[level].pop()
        except: 
            # print("Making new level")
            data.append(list())
        if root:
            # print(f"Current level is on {level}")
            data[level].append(root.val)
            # print(f"The solution right now: {data}")
            if root.left or root.right:
                if root.left: 
                    # print("Up a level")
                    self.levelOrder(root.left, data, level+1)
                if root.right: 
                    # print("Up a level")
                    self.levelOrder(root.right, data, level+1)
                # print("Down a level")
        return data

    def maxDepth(self, root, answer=1, current_level=1):
        # print(f"Current Answer is so far: {answer}")
        # print(f"Current level is: {level}")
        if root:
            if root.left or root.right:
                if answer <= current_level: answer += 1
                if root.left is not None: 
                    # print("Going through Left")
                    answer = self.maxDepth(root.right, answer, current_level+1)
                if root.right is not None: 
                    # print("Going through Right")
                    answer = self.maxDepth(root.right, answer, current_level+1)
        else: return 0
        return answer
