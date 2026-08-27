class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visit = set()
        cycle = set()
        output = []

        hsmp = {i:[] for i in range(numCourses)}

        for crs, pre in  prerequisites:
            hsmp[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visit:
                return True

            cycle.add(crs)

            for pre in hsmp[crs]:
                if not dfs(pre): return False

            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        
        for pre in range(numCourses):
            if not dfs(pre): return []
        return output