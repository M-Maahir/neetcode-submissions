class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        par = [i for i in range(n)]
        rank = [1]*n

        def find(u):
            res = u

            while res != par[res]:
                res = par[res]

            return res
        

        def union(u, v):

            f1, f2 = find(u), find(v)

            if f1 == f2:
                return 0

            if rank[f2] > rank[f1]:
                par[f1] = f1
                rank[f2] = rank[f1]

            else:
                par[f2] = f1
                rank[f1] = rank[f2]

            return 1



        res = n

        for u,v in edges:
            res -= union(u,v)

        return res
       