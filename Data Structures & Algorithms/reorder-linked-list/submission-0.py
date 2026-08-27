# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
        
        
        current = slow.next
        prv = slow.next = None

        while current:
            temp = current.next
            current.next = prv
            prv = current
            current = temp
        
        current = prv
        first = head

        while current:
            temp1, temp2 = first.next, current.next
            first.next = current
            current.next = temp1
            first, current = temp1, temp2