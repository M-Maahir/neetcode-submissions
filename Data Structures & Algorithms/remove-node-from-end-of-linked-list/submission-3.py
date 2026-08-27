# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(27, head)
        curr = dummy
        tail = head

        while n > 0:
            tail = tail.next
            n -= 1

        while tail: 
            curr = curr.next
            tail = tail.next
        
        curr.next = curr.next.next

        return dummy.next

        
        