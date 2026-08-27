class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos = [(p, s) for p,s in zip(position, speed)]
        stack = []
        pos.sort(reverse = True)

        for p, s in pos:
            t = (target - p)/s
            if stack and stack[-1] >= t:
                continue
            stack.append(t)

        return len(stack)

        

        