from algo.tests.challenge_tester import challengeAlgorithms
from algo.tests.array_tester import arrayAlgorthims
from algo.tests.linked_list_tester import linkedlistAlgorithms


# Actually running the tests
def run() -> None:
    # Maybe add in a prompt to run individual programs to test out
    challengeAlgorithms()
    arrayAlgorthims()
    linkedlistAlgorithms()
