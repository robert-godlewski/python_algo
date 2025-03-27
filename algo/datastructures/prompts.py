from algo.datastructures.tools import skipTest
from algo.tests.challenge_tester import challengeAlgorithms
from algo.tests.array_tester import arrayAlgorthims
from algo.tests.string_tester import stringAlgorithms
from algo.tests.recursion1_tester import recursion1Algorithms
from algo.tests.linked_list_tester import linkedlistAlgorithms
from algo.tests.hashset_tester import hashsetAlgorithms
from algo.tests.hashmap_tester import hashmapAlgorithms
from algo.tests.queue_tester import queueAlgorithms
from algo.tests.stack_tester import stackAlgorithms
from algo.tests.binary_tree_tester import btAlgorithms
from algo.tests.binary_search_tester import bsAlgorithms
from algo.tests.bst_tester import btsAlgorithms
from algo.tests.recursion2_tester import recursion2Algorithms
# temporarily keep
from algo.algorithmtemplates.sorting_templates import runSortingTests


# List of prompts
prompts = [
    "Challenge",
    # Data Structures
    "Array","String","Hash Map","Hash Set","Linked List","Queue","Stack","Heap","Binary Tree","Trie","N-ary Tree","Graph",
    # Algorithms
    "Binary Search","Recursion 1","Recursion 2","Binary Tree Search",
    # Testing sort algorithms
    "Sort Algorithms"
]

# Running the tests based off of prompt
def runPrompt(prompt: int) -> None:
    if prompt < 0: print("Please use a number 0 and above, try again.")
    elif prompt == 0: challengeAlgorithms()
    # Data Structures
    elif prompt == 1: arrayAlgorthims()
    elif prompt == 2: stringAlgorithms()
    elif prompt == 3: hashmapAlgorithms()
    elif prompt == 4: hashsetAlgorithms()
    elif prompt == 5: linkedlistAlgorithms()
    elif prompt == 6: queueAlgorithms()
    elif prompt == 7: stackAlgorithms()
    elif prompt == 8: skipTest("Heap")
    elif prompt == 9: btAlgorithms()
    elif prompt == 10: skipTest("Trie")
    elif prompt == 11: skipTest("N-ary Tree")
    elif prompt == 12: skipTest("Graph")
    # Algorithms
    elif prompt == 13: bsAlgorithms()
    elif prompt == 14: recursion1Algorithms()
    elif prompt == 15: recursion2Algorithms()
    elif prompt == 16: btsAlgorithms()
    elif prompt == 17: runSortingTests()
    else: print("Please use a smaller number, try again.")
