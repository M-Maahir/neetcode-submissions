class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        s = [[p,s] for p,s in zip(position, speed)]
        s.sort(reverse=True)
        stack = []

        for p,s in s:
            time = (target - p)/s

            if stack and stack[-1] >= time:
                continue

            stack.append(time)

        return len(stack)
