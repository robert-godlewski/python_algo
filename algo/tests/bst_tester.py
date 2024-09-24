# Tools needed
from algo.datastructures.tools import titleline, thinline
from algo.datastructures.binary_tree import TreeNode
from algo.solutions.bst_solutions import Solution


solver = Solution()
traversal = None


# Main function to run all tests - Add this into main
def btsAlgorithms() -> None:
    titleline("Testing binary search tree algorithms")

    bst1 = TreeNode(2)
    bst1.left = TreeNode(1)
    bst1.right = TreeNode(3)
    bst2 = TreeNode(5)
    bst2.left = TreeNode(1)
    bst2.right = TreeNode(4)
    bst2.right.left = TreeNode(3)
    bst2.right.right = TreeNode(6)
    bst3 = TreeNode(2)
    bst3.left = TreeNode(2)
    bst3.right = TreeNode(2)
    bst4 = TreeNode(5)
    bst4.left = TreeNode(4)
    bst4.right = TreeNode(6)
    bst4.right.left = TreeNode(3)
    bst4.right.right = TreeNode(7)

    validBSTtest(bst1)
    validBSTtest(bst2)
    validBSTtest(bst3)
    validBSTtest(bst4)


# Testing isValidBST - Fix this
def validBSTtest(root: TreeNode) -> None:
    print("...")