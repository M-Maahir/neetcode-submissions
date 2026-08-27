class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        fast = 0
        slow = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        
        slow1 = 0

        while True:
            slow1 = nums[slow1]
            slow = nums[slow]
            if slow == slow1:
                return slow

        