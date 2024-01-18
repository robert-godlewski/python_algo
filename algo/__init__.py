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
# temporarily keep
from algo.datastructures.sorting_templates import *


# Actually running the tests
def run() -> None:
    print("Welcome to python algorithm practice")
    running_algos = True
    prompt = None
    while running_algos and not prompt:
        print("Pick one of these numbers to run a group of tests:")
        # A list of tests Robert has solved in leetcode
        prompt_list = [
            "Challenge Problems",
            "Array Problems",
            "Recursion 1 Problems",
            "Linked List Problems",
            "Hash Set Problems",
            "Hash Map Problems",
            "Queue Problems",
            "Stack Problems",
            "Binary Tree Problems",
            "Binary Search Problems",
            "Test Sort Algorithm"
        ]
        i = 0
        while i < len(prompt_list):
            print(f"{i+1} = {prompt_list[i]}")
            i += 1
        prompt = input("Choose one of the numbers above: ")
        try:
            prompt_int = int(prompt)
            if prompt_int <= 0:
                print(f"'{prompt}' has to be a positive number, please try again.")
                prompt = None
            elif prompt_int == 1:
                challengeAlgorithms()
            elif prompt_int == 2:
                arrayAlgorthims()
            elif prompt_int == 3:
                recursion1Algorithms()
            elif prompt_int == 4:
                linkedlistAlgorithms()
            elif prompt_int == 5:
                hashsetAlgorithms()
            elif prompt_int == 6:
                hashmapAlgorithms()
            elif prompt_int == 7:
                queueAlgorithms()
            elif prompt_int == 8:
                stackAlgorithms()
            elif prompt_int == 9:
                btAlgorithms()
            elif prompt_int == 10:
                bsAlgorithms()
            elif prompt_int == 11:
                bubbleTest()
                selectionTest()
                insertionTest()
                # quickTest()
                mergeTest()
            else:
                print(f"'{prompt}' has to be a smaller number, please try again.")
                prompt = None
        except ValueError:
            print(f"'{prompt}' is not a number, please try again.")
            prompt = None
        if prompt:
            prompt2 = input("Do you want to go again (y/n)? ")
            if prompt2 == "n":
                print("Good By")
                running_algos = False
            prompt = None
