class Solution:
    def isValid(self, s: str) -> bool:

        hsmp ={
                "]":"[",
                "}":"{",
                ")":"("
            }

        stack = []


        for c in s:
            if c in hsmp:
                if stack and stack[-1] == hsmp[c]:
                    stack.pop()
                else: return False
            
            else: stack.append(c)

        print(stack)
        

        return False if stack else True 