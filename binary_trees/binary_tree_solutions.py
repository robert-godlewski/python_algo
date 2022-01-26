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



# Testing area:
solver = Solution()

node1 = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
node2 = None
node3 = TreeNode(1)
node4 = TreeNode(3, left=TreeNode(1), right=TreeNode(2))

# For preorder
print('Preorder Traversal:')
print('=========New Root=========')
print("root = [1, None, 2, 3]")
print("Solution is:", solver.preorderTraversal(node1))
print('=========New Root=========')
print("root = []")
print("Solution is:", solver.preorderTraversal(node2))
print('=========New Root=========')
print("root = [1]")
print("Solution is:", solver.preorderTraversal(node3))
print('=========New Root=========')
print("root = [3, 1, 2]")
print("Solution is:", solver.preorderTraversal(node4))
print()
# For inorder
print('Inorder Traversal:')
print('=========New Root=========')
print("root = [1, None, 2, 3]")
print("Solution is:", solver.inorderTraversal(node1))
print('=========New Root=========')
print("root = []")
print("Solution is:", solver.inorderTraversal(node2))
print('=========New Root=========')
print("root = [1]")
print("Solution is:", solver.inorderTraversal(node3))
print('=========New Root=========')
print("root = [3, 1, 2]")
print("Solution is:", solver.inorderTraversal(node4))
print()
# For postorder
print('Postorder Traversal:')
print('=========New Root=========')
print("root = [1, None, 2, 3]")
print("Solution is:", solver.postorderTraversal(node1))
print('=========New Root=========')
print("root = []")
print("Solution is:", solver.postorderTraversal(node2))
print('=========New Root=========')
print("root = [1]")
print("Solution is:", solver.postorderTraversal(node3))
print('=========New Root=========')
print("root = [3, 1, 2]")
print("Solution is:", solver.postorderTraversal(node4))
print()
