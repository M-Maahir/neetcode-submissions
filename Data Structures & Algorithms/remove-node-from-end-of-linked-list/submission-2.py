# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(23, head)
        temp = dummy

        curr = head

        for _ in range(n):
            curr = curr.next 

        while curr:
            curr = curr.next
            temp = temp.next

        temp.next = temp.next.next

        return dummy.next



        
