class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        stack = []

        def dfs(l, r, n):
            if l == r == n:
                res.append("".join(stack))
                return 

            if l < n:
                stack.append("(")
                dfs(l + 1, r, n)
                stack.pop()

            if r < l:
                stack.append(")")
                dfs(l, r + 1, n)
                stack.pop()

            
        dfs(0, 0, n)
        return res

        