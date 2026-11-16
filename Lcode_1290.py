# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        binary = 0
        curr = head

        while curr:
            binary = (binary << 1) | curr.val
            curr = curr.next

        return binary

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

    values = [1,0,1]

    head = create_linkedlist(values)

    print("Original Linked List:")
    display(head)

    solution = Solution()

    out = solution.getDecimalValue(head)

    print(out)


    