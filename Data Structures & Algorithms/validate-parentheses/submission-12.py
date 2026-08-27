class Solution:
    def isValid(self, s: str) -> bool:

        hsmp ={
                "]":"[",
                "}":"{",
                ")":"("
            }

        stack = []

        for i in range(len(s)):
            if s[i] in hsmp:
                if stack and stack[-1] == hsmp[s[i]]:
                    stack.pop()
                else: return False
                
            else:stack.append(s[i])
        
        return True if len(stack) == 0 else False