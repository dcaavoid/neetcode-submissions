class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adjacency List (Hash Map) + DFS/BFS
        prereqMap = {i: [] for i in range(numCourses)}  # i: list of prerequisites for i.
        visited = set()   # courses that are currently waiting for prerequsite to be finished.
        for crs, pre in prerequisites:
            prereqMap[crs].append(pre)
        
        # Return whether crs can be finished.
        def dfs(crs: int) -> bool:
            # Base case
            # 1. No prerequisite
            if prereqMap[crs] == []:
                return True
            # 2. Cycle in prerequisite.
            if crs in visited:
                return False
            
            # Recursively if crs's prerequisites can be finished.
            visited.add(crs)
            for pre in prereqMap[crs]:
                if not dfs(pre):
                    return False
            
            prereqMap[crs] = []
            visited.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True

        