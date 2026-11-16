
# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


# Create linked list
def create_linkedlist(values):

    if not values:
        return None

    head = ListNode(values[0])
    curr = head

    for value in values[1:]:
        curr.next = ListNode(value)
        curr = curr.next

    return head


# Display linked list
def display(head):

    curr = head

    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next

    print("None")


# Main program
if __name__ == "__main__":

    values = [1, 2, 3, 4, 5]

    head = create_linkedlist(values)

    print("Original Linked List:")
    display(head)

    solution = Solution()

    middle = solution.middleNode(head)

    print("Middle Node:")
    display(middle)
