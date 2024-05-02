from src.datadebug import logger

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return str(self.value)

def merge_two_lists(l1, l2):
    dummy = ListNode(" ")
    tail = dummy

    logger.create_node(dummy, display=True)

    while l1 and l2:

        logger.add_pointers(
            [tail, dummy, l2, l1],
            ["tail", "dummy", "l2", "l1"],
            save_pointers=False
        )

        if l1.value < l2.value:
            logger.delete_edge(tail, tail.next)
            tail.next = l1
            logger.add_edge(tail, l1, display=False)
            l1 = l1.next
        else:
            logger.delete_edge(tail, tail.next)
            tail.next = l2
            logger.add_edge(tail, l2, display=False)
            l2 = l2.next #BUG: should be l2.next
        tail = tail.next

    tail.next = l1 or l2

    logger.add_edge(tail, tail.next)

    return dummy.next


if __name__ == "__main__":

    l1_values = [1, 5, 10]
    l2_values = [2, 3, 6]

    # convert l1_values to a linked list
    l1_head = ListNode(l1_values[0])
    current = l1_head
    for value in l1_values[1:]:
        current.next = ListNode(value)
        logger.add_edge(current, current.next, display=False)
        current = current.next

    # convert l2_values to a linked list
    l2_head = ListNode(l2_values[0])
    current = l2_head
    for value in l2_values[1:]:
        current.next = ListNode(value)
        logger.add_edge(current, current.next, display=False)
        current = current.next

    logger.visualize()

    # MERGE TWO LISTS
    result = merge_two_lists(l1_head, l2_head)

    # print the result
    current = result
    print("RESULT:")
    while current:
        print(current.value)
        current = current.next