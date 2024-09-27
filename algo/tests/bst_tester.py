# Tools needed
from algo.datastructures.tools import titleline, thinline
from algo.datastructures.binary_tree import TreeNode
from algo.solutions.bst_solutions import Solution
from algo.solutions.binary_tree_solutions import Solution as bts


solver = Solution()
traversal = None
btPrint = bts()

# Used to print out the binary trees
def msgTree(root: TreeNode) -> str:
    treeArr = btPrint.levelOrder(root)
    return f"Binary Tree: {treeArr}"


# Main function to run all tests
def btsAlgorithms() -> None:
    titleline("Testing binary search tree algorithms")

    # Good tree
    bst1 = TreeNode(2)
    bst1.left = TreeNode(1)
    bst1.right = TreeNode(3)
    # Bad tree
    bst2 = TreeNode(5)
    bst2.left = TreeNode(1)
    bst2.right = TreeNode(4)
    bst2.right.left = TreeNode(3)
    bst2.right.right = TreeNode(6)
    # Bad tree
    bst3 = TreeNode(2)
    bst3.left = TreeNode(2)
    bst3.right = TreeNode(2)
    # Bad tree
    bst4 = TreeNode(5)
    bst4.left = TreeNode(4)
    bst4.right = TreeNode(6)
    bst4.right.left = TreeNode(3)
    bst4.right.right = TreeNode(7)
    # Good tree
    bst5 = TreeNode(4)
    bst5.left = bst1
    bst5.right = TreeNode(7)
    # Good tree
    bst6 = TreeNode(5)
    bst6.left = TreeNode(3)
    bst6.left.left = TreeNode(2)
    bst6.left.right = TreeNode(4)
    bst6.right = TreeNode(6)
    bst6.right.right = TreeNode(7)

    validBSTtest(bst1)
    validBSTtest(bst2)
    validBSTtest(bst3)
    validBSTtest(bst4)
    validBSTtest(bst5)
    validBSTtest(None)
    thinline()

    bstSearchTest(bst1,3)
    bstSearchTest(bst5, 2)
    bstSearchTest(bst5, 5)
    thinline()

    bstInsertTest(bst5,5)
    thinline()

    bstDeletionTest(bst5,5)
    bstDeletionTest(bst6,3)
    bstDeletionTest(bst6,5)
    bstDeletionTest(bst6,5)


# Testing isValidBST
def validBSTtest(root: TreeNode) -> None:
    # treePrint = btPrint.levelOrder(root=root)
    # print("Binary Tree:")
    # print(treePrint)
    print(msgTree(root))
    ans = solver.isValidBST(root)
    print(f"Is this tree valid? {ans}")

# Testing searchBST
def bstSearchTest(root: TreeNode, val: int) -> None:
    print(f"Can I find {val} in {msgTree(root)}")
    ans = solver.searchBST(root, val)
    print(f"The answer is {msgTree(ans)}")

# Testing insertIntoBST
def bstInsertTest(root: TreeNode, val: int) -> None:
    print(f"Inserting {val} into the following {msgTree(root)}")
    ans = solver.insertIntoBST(root, val)
    print(f"The answer is {msgTree(ans)}")

# Testing deleteNode
def bstDeletionTest(root: TreeNode, key: int) -> None:
    print(f"Removing {key} from the {msgTree(root)}")
    ans = solver.insertIntoBST(root, key)
    print(f"Updated {msgTree(ans)}")
