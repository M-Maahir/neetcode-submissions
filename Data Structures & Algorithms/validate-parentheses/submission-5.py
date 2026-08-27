class Solution:
    def isValid(self, s: str) -> bool:

        hsmp ={
                "]":"[",
                "}":"{",
                ")":"("
            }
        
        stack = []

        for i in s:
            if i in hsmp:
                if stack and hsmp[i] == stack[-1]:
                    stack.pop()
                else: return False

            else:
                stack.append(i)

        return len(stack)==0

        