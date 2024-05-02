class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f"{self.value} -> {self.next}"

def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:

        print("l1:", l1)
        print("l2:", l2)
        print("final:", dummy.next)
        print()

        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l1  #BUG: should be l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next


if __name__ == "__main__":

    l1_values = [1, 5, 10]
    l2_values = [2, 3, 6]

    # convert l1_values to a linked list
    l1_head = ListNode(l1_values[0])
    current = l1_head
    for value in l1_values[1:]:
        current.next = ListNode(value)
        current = current.next

    # convert l2_values to a linked list
    l2_head = ListNode(l2_values[0])
    current = l2_head
    for value in l2_values[1:]:
        current.next = ListNode(value)
        current = current.next

    # MERGE TWO LISTS
    result = merge_two_lists(l1_head, l2_head)

    # print the result
    current = result
    print("RESULT:")
    while current:
        print(current.value)
        current = current.next