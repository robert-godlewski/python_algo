# A list of prompts based off of problems Robert has solved in leetcode
from algo.datastructures.prompts import prompts, runPrompt


# Actually running the tests
def run() -> None:
    print("Welcome to python algorithm practice")
    running_algos = True
    prompt = None
    while running_algos and not prompt:
        print("Pick one of these numbers to run a group of tests:")
        # Looking through the prompts
        i = 0
        while i < len(prompts):
            print(f"{i} for {prompts[i]} Problems.")
            i += 1
        prompt = input("Choose one of the numbers above: ")
        try:
            prompt_int = int(prompt)
            # print(f'input = {type(prompt_int)}: {prompt_int}')
            runPrompt(prompt_int)
        except ValueError:
            print(f"'{prompt}' is not a number, please try again.")
        # Deciding to either stop or continue
        prompt = input("Do you want to go again (y/n)? ")
        if prompt == "n":
            print("Good By")
            running_algos = False
        prompt = None
