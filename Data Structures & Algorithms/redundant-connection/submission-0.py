class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        par = [i for i in range(len(edges) + 1)]
        rank = [1]*(len(edges) +1 )


        def find(u):
            res = u 

            while res != par[res]:
                res = par[res]
            return res


        def union(u,v):

            p1, p2 = find(u), find(v)

            if p1 == p2:
                return False

            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p1] += rank[p2]

            else:
                par[p2] = p1 
                rank[p1] += rank[p2]

            return True


        for u,v in edges:
            if union(u,v) == False:
                return [u,v]