'''
Time: O(n)
Space: O(1)

n = Length of array
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        node = head
        while node and node.next:
            next_node = node.next

            # Skip if same val
            if node.val == next_node.val:
                node.next = next_node.next
            else:
                node = next_node
        return head
        