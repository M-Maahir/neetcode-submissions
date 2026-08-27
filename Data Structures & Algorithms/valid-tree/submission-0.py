class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        vst = set()

        adj = {i:[] for i in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        def dfs(node, prv):
            if node in vst: return False

            vst.add(node)

            for i in adj[node]:
                if prv == i:
                    continue
                
                if not dfs(i, node): return False

            return True

        return dfs(0, -1) and len(vst) == n