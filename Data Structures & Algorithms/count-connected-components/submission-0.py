class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}

        visit = set()

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        def dfs(i):
            if i in visit:
                return

            visit.add(i)

            for pre in adj[i]:
                dfs(pre)

        
        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
        

        return count

        