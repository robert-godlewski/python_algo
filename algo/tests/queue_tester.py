# Tools needed
from algo.datastructures.tools import titleline, thinline
from algo.datastructures.queue import LinkedQueue, printLQ


# Main function to run all tests
def queueAlgorithms() -> None:
    titleline("Testing the linked queue class")

    q = LinkedQueue()
    print(f"Created New Queue")
    print(f"Is the queue empty? {q.isEmpty()}")
    print(printLQ(q.head))
    thinline()
    q.enQueue(1)
    print(printLQ(q.head))
    print(f"Is the queue empty? {q.isEmpty()}")
    thinline()
    q.enQueue(2)
    print(printLQ(q.head))
    thinline()
    q.addAtHead(3)
    print(printLQ(q.head))
    thinline()
    q.addAtIndex(3,3)
    print(printLQ(q.head))
    thinline()
    rem = q.deQueue()
    print(printLQ(q.head))
    print(f"Removed {rem} from the queue")
