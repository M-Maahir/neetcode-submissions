class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)+1
        par = [i for i in range(n)]
        rank = [1] * n

        def find(u):
            res = u

            while res != par[res]:
                res = par[res]

            return res

        
        def union(u,v):
            f1, f2 = find(u), find(v)

            if f1 == f2:
                return False

            if rank[f2] > rank[f1]:
                par[f1] = f2
                rank[f2] += rank[f1] 

            else:
                par[f2] = f1
                rank[f1] += rank[f2]

            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]
                