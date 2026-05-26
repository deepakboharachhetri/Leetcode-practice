class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):

        # Fake starter node
        dummy = ListNode()

        # Tail helps build result list
        tail = dummy

        # Traverse both lists
        while list1 and list2:

            # Pick smaller value
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # Move tail forward
            tail = tail.next

        # Attach remaining nodes
        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        # Return head of merged list
        return dummy.next


# -----------------------------------
# Helper function to create linked list
# -----------------------------------

def create_linked_list(arr):

    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# -----------------------------------
# Helper function to print linked list
# -----------------------------------

def print_linked_list(head):

    current = head

    while current:
        print(current.val, end=" -> ")
        current = current.next

    print("None")


# -----------------------------------
# TEST
# -----------------------------------

list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

solution = Solution()

merged = solution.mergeTwoLists(list1, list2)

print("Merged Linked List:")
print_linked_list(merged)