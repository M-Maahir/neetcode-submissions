# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head 
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        curr = slow.next
        slow.next = None
        prv = None

        while curr:
            temp = curr.next
            curr.next = prv
            prv = curr
            curr = temp

        first = head
        sec = prv
        
        while sec:
            tmp1, tmp2 = first.next, sec.next
            first.next = sec
            sec.next = tmp1

            first = tmp1
            sec = tmp2
        




        