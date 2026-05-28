'''
=============== Complexity ===============
Time:  O(n)
Space: O(1)

n = Length of array

=============== Algorithm ===============
1. Inspect first node
2. If next node same val as current, skip node
3. If different, inspect next node
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_duplicates(head: ListNode | None) -> ListNode | None:
    node = head
    while node and node.next:
        next_node = node.next

        # Skip if same val
        if node.val == next_node.val:
            node.next = next_node.next
        else:
            node = next_node
    return head
    