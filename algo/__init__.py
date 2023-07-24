from algo.tests.challenge_tester import challengeAlgorithms
from algo.tests.array_tester import arrayAlgorthims
from algo.tests.recursion1_tester import recursion1Algorithms
from algo.tests.linked_list_tester import linkedlistAlgorithms
from algo.tests.hashset_tester import hashsetAlgorithms
from algo.tests.hashmap_tester import hashmapAlgorithms
from algo.tests.queue_tester import queueAlgorithms
from algo.tests.stack_tester import stackAlgorithms
from algo.tests.binary_tree_tester import btAlgorithms
from algo.tests.binary_search_tester import bsAlgorithms


# Actually running the tests
def run() -> None:
    print("Welcome to python algorithm practice")
    running_algos = True
    prompt = None
    while running_algos and not prompt:
        print("Pick one of these numbers to run a group of tests:")
        print("1 = Challenge Problems")
        print("2 = Array Problems")
        print("3 = Recursion 1 Problems")
        print("4 = Linked List Problems")
        print("5 = Hash Set Problems")
        print("6 = Hash Map Problems")
        print("7 = Queue Problems")
        print("8 = Stack Problems")
        print("9 = Binary Tree Problems")
        print("10 = Binary Search Problems")
        prompt = input("Choose one of the numbers above: ")
        if int(prompt) == 1:
            challengeAlgorithms()
        elif int(prompt) == 2:
            arrayAlgorthims()
        elif int(prompt) == 3:
            recursion1Algorithms()
        elif int(prompt) == 4:
            linkedlistAlgorithms()
        elif int(prompt) == 5:
            hashsetAlgorithms()
        elif int(prompt) == 6:
            hashmapAlgorithms()
        elif int(prompt) == 7:
            queueAlgorithms()
        elif int(prompt) == 8:
            stackAlgorithms()
        elif int(prompt) == 9:
            btAlgorithms()
        elif int(prompt) == 10:
            bsAlgorithms()
        else:
            print("Not an option please choose one of the given numbers")
        prompt = None
        prompt2 = input("Do you want to go again (y/n)? ")
        if prompt2 == "n":
            print("Good By")
            running_algos = False
