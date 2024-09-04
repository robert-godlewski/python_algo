# Tools needed
from algo.datastructures.tools import titleline, thinline
from algo.datastructures.binary_tree import TreeNode
from algo.solutions.binary_tree_solutions import Solution


solver = Solution()


# Main function to run all tests
def btAlgorithms() -> None:
    titleline("Testing binary tree algorithms")

    # Binary trees to test out
    bt1 = TreeNode(1)
    bt1.right = TreeNode(2)
    bt1.right.left = TreeNode(3)
    btsingle = TreeNode(1)
    bt2 = TreeNode(3)
    bt2.left = TreeNode(9)
    bt2.right = TreeNode(20)
    bt2.right.left = TreeNode(15)
    bt2.right.right = TreeNode(7)
    bt3 = TreeNode(1)
    bt3.right = TreeNode(2)
    btsymmetry = TreeNode(1)
    btsymmetry.left = TreeNode(2, TreeNode(3), TreeNode(4))
    btsymmetry.right = TreeNode(2, TreeNode(4), TreeNode(3))
    bt4 = TreeNode(5)
    bt4.left = TreeNode(4)
    bt4.left.left = TreeNode(11, left=TreeNode(7), right=TreeNode(2))
    bt4.right = TreeNode(8)
    bt4.right.left = TreeNode(13)
    bt4.right.right = TreeNode(4, right=TreeNode(1))
    bt5 = TreeNode(1) # root
    bt5.left = TreeNode(2, left=TreeNode(4))
    bt5.left.right = TreeNode(5, left=TreeNode(6), right=TreeNode(7))
    bt5.right = TreeNode(3)
    bt5.right.right = TreeNode(8, left=TreeNode(9))

    preorderTraversalTest(bt1)
    preorderTraversalTest(bt2)
    preorderTraversalTest(bt3)
    preorderTraversalTest(bt4)
    preorderTraversalTest(bt5)
    preorderTraversalTest(None)
    preorderTraversalTest(btsingle)
    thinline()

    inorderTraversalTest(bt1)
    inorderTraversalTest(bt2)
    inorderTraversalTest(bt3)
    inorderTraversalTest(bt4)
    inorderTraversalTest(bt5)
    inorderTraversalTest(None)
    inorderTraversalTest(btsingle)
    thinline()

    postorderTraversalTest(bt1)
    postorderTraversalTest(bt2)
    postorderTraversalTest(bt3)
    postorderTraversalTest(bt4)
    postorderTraversalTest(bt5)
    postorderTraversalTest(None)
    postorderTraversalTest(btsingle)
    # thinline()

    # levelOrderTest(bt1)
    # levelOrderTest(bt2)
    # levelOrderTest(bt3)
    # levelOrderTest(None)
    # levelOrderTest(btsingle)
    # thinline()

    # maxDepthTest(bt1)
    # maxDepthTest(bt2)
    # maxDepthTest(bt3)
    # maxDepthTest(None)
    # maxDepthTest(btsingle)
    # thinline()

    # symmetricTest(bt1)
    # symmetricTest(btsymmetry)
    # thinline()

    # hasPathSumTest(bt4, 22)
    # hasPathSumTest(bt5, 5)
    # hasPathSumTest(None, 0)


# Testing preorderTraversal
def preorderTraversalTest(node) -> None:
    answer = solver.preorderTraversal(node)
    print(f"The preorder tree = {answer}")

# Testing inorderTraversal
def inorderTraversalTest(node) -> None:
    answer = solver.inorderTraversal(node)
    print(f"The inorder tree = {answer}")

# Testing postorderTraversal
def postorderTraversalTest(node) -> None:
    answer = solver.postorderTraversal(node)
    print(f"The postorder tree = {answer}")

# Testing levelOrder
def levelOrderTest(node) -> None:
    answer = solver.levelOrder(node)
    print(f"The level order tree = {answer}")

# Testing maxDepth
def maxDepthTest(node) -> None:
    answer = solver.maxDepth(node)
    print(f"The depth of the tree = {answer}")

# Testing isSymmetric
def symmetricTest(node) -> None:
    answer = solver.isSymmetric(node)
    print(f"Is the tree symmetric? {answer}")

# Testing hasPathSum
def hasPathSumTest(node, target: int) -> None:
    print(f"Tree = {solver.inorderTraversal(node)}")
    answer = solver.hasPathSum(node, target)
    print(f"Is there a root-leaf sum = {target}? {answer}")
