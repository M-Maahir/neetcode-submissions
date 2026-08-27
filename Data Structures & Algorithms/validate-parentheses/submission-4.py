class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        hsmp = {
            "]":"[",
            "}":"{",
            ")":"("
        }

        for i in s:
            if i in hsmp:
                if stack and stack[-1] == hsmp[i]:
                    stack.pop()
                else: return False
            else:
                stack.append(i)
        

        return False if stack else True
        