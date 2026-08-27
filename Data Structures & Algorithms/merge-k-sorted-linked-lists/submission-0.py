# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists and len(lists) == 0:
            return None
        
        while len(lists) > 1:
            res = []

            for i in range(0, len(lists), 2):
                ls1 = lists[i]
                ls2 = lists[i+1] if i + 1 < len(lists) else None

                res.append(self.merge(ls1, ls2))
            
            lists = res
        
        return lists[0]

    
    def merge(self, ls1, ls2):

        dummy = ListNode()
        tail = dummy

        while ls1 and ls2:
            if ls1.val < ls2.val:
                tail.next = ls1
                ls1 = ls1.next
            else:
                tail.next = ls2
                ls2 = ls2.next
            tail = tail.next

        if ls1:
            tail.next = ls1
        
        if ls2:
            tail.next = ls2
        
        return dummy.next






        