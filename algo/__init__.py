from algo.tests.challenge_tester import challengeAlgorithms
from algo.tests.array_tester import arrayAlgorthims
from algo.tests.linked_list_tester import linkedlistAlgorithms
from algo.tests.recursion1_tester import recursion1Algorithms
from algo.tests.queue_tester import queueAlgorithms


# Actually running the tests
def run() -> None:
    # Maybe add in a prompt to run individual programs to test out
    challengeAlgorithms()
    arrayAlgorthims()
    linkedlistAlgorithms()
    recursion1Algorithms()
    queueAlgorithms()
