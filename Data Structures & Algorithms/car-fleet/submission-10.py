class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos = [(p, s) for p,s in zip(position, speed)]

        #be mid
        stack = []
        pos.sort(reverse = True)

        for p, s in pos:
            t = (target - p)/s
            if not stack or stack[-1] < t:
                stack.append(t)

        return len(stack)

        

        