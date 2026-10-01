# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # Find Middle
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next 
            fast=fast.next.next 
        # Split list into two 
        head2 = slow.next
        slow.next = None
        # Reverse second list
        prev=None
        current=head2
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        head2=prev
        # Merge them together
        l1 = head
        l2 = head2
        while l2:
            next1=l1.next
            next2=l2.next
            l1.next=l2 
            l2.next=next1
            l1 = next1
            l2 = next2