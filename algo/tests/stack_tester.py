# Tools needed
from algo.datastructures.tools import titleline, thinline
from algo.datastructures.stack import LinkedStack, printLS


# Main function to run all tests
def stackAlgorithms() -> None:
    titleline("Testing the linked stack class")

    s = LinkedStack()
    print(f"Created New Stack")
    print(f"Is the stack empty? {s.isEmpty()}")
    print(printLS(s.head))
    thinline()
    s.push(1)
    print(printLS(s.head))
    print(f"Is the stack empty? {s.isEmpty()}")
    thinline()
    s.push(2)
    print(printLS(s.head))
    thinline()
    s.addAtHead(3)
    print(printLS(s.head))
    thinline()
    s.addAtIndex(3,3)
    print(printLS(s.head))
    thinline()
    rem = s.pop()
    print(printLS(s.head))
    print(f"Removed {rem} from the stack")
