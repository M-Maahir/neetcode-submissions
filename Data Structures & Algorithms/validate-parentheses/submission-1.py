class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hash_map={")":"(",
                    "]":"[",
                    "}":"{",
                    }

        for i in s:
            if i in hash_map:
                if stack and stack[-1]==hash_map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return False if stack else True
            
        