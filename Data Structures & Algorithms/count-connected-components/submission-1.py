class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        count = 0

        def dfs(node):

            if node in visit:
                return 
            
            visit.add(node)

            for neigh in adj[node]:
                dfs(neigh)

        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
        
        return count