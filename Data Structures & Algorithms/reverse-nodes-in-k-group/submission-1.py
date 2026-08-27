# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(27, head)
        tail = dummy

        while True:
            kth = self.kths(tail, k)

            if kth is None:
                break
            
            nextStart = kth.next

            curr = tail.next 
            prv = nextStart
            while curr != nextStart:
                temp = curr.next
                curr.next = prv
                prv = curr
                curr = temp
            
            temp = tail.next
            tail.next = kth
            tail = temp
        
        return dummy.next
    
    def kths(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -=1 
        return curr


        
        