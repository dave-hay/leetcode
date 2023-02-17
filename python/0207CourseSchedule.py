class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for i, v in prerequisites:
            adj[i].append(v)

        # all courses along curr path
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if adj[crs] == []:
                return True

            visit.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False

            visit.remove(crs)
            adj[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
