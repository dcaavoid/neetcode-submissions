class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological sort with DFS
        prereq = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        # For each course:
        # 1. taken: courses that can have been taken without any cycle.
        # 2. cycle: track if the current course's prerequisites have cycle.
        # 3. res: order to take courses
        taken, cycle = set(), set()
        res = []

        # Return if course crs's prerequisites have cycle.
        def dfs(crs: int) -> bool:
            # Base case
            if crs in cycle:
                return False
            if crs in taken:
                return True
            
            # Recursive
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            taken.add(crs)
            res.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
            
        return res