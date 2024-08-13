# Needed tools for formating terminal messages

# Printing out different algorithm topics
def titleline(title: str) -> None:
    print("============")
    print(title)
    print("============")

# Printing out the different tests
def thinline() -> None:
    print("------------")

# Printing out that we are skipping a prompt
def skipTest(title: str) -> None:
    titleline(f"We currently don't have any {title} Problems to test right now.")
