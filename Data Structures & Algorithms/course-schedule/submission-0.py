class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hmp = { i:[] for i in range(numCourses)}

        visit = set()

        for crs, pre in prerequisites:
            hmp[crs].append(pre)

        def dfs(crs):

            if crs in visit:
                return False

            if hmp[crs] == []:
                return True

            visit.add(crs)

            for pre in hmp[crs]:
                if not dfs(pre): return False

            visit.remove(crs)
            hmp[crs] = []
            return True




        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True

        