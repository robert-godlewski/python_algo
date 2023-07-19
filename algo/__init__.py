from algo.tests.challenge_tester import challengeAlgorithms
from algo.tests.array_tester import arrayAlgorthims
from algo.tests.recursion1_tester import recursion1Algorithms
from algo.tests.linked_list_tester import linkedlistAlgorithms
from algo.tests.hashset_tester import hashsetAlgorithms
from algo.tests.hashmap_tester import hashmapAlgorithms
from algo.tests.queue_tester import queueAlgorithms
from algo.tests.stack_tester import stackAlgorithms
from algo.tests.binary_tree_tester import btAlgorithms


# Actually running the tests
def run() -> None:
    # Maybe add in a prompt to run individual programs to test out
    challengeAlgorithms()
    arrayAlgorthims()
    recursion1Algorithms()
    linkedlistAlgorithms()
    hashsetAlgorithms()
    hashmapAlgorithms()
    queueAlgorithms()
    stackAlgorithms()
    btAlgorithms()
