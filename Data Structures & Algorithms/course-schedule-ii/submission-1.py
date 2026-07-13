class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Version 1: Topological sort with DFS
        # prereq = {i: [] for i in range(numCourses)}
        # for crs, pre in prerequisites:
        #     prereq[crs].append(pre)
        
        # # For each course:
        # # 1. taken: courses that can have been taken without any cycle.
        # # 2. cycle: track if the current course's prerequisites have cycle.
        # # 3. res: order to take courses
        # taken, cycle = set(), set()
        # res = []

        # # Return if course crs's prerequisites have cycle.
        # def dfs(crs: int) -> bool:
        #     # Base case
        #     if crs in cycle:
        #         return False
        #     if crs in taken:
        #         return True
            
        #     # Recursive
        #     cycle.add(crs)
        #     for pre in prereq[crs]:
        #         if not dfs(pre):
        #             return False
            
        #     cycle.remove(crs)
        #     taken.add(crs)
        #     res.append(crs)
        #     return True

        # for c in range(numCourses):
        #     if not dfs(c):
        #         return []
            
        # return res

        # ------------------------------------------------------------------------------------
        # Version 2: BFS (start from courses with no prerequisite)
        preToCrs = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses   # Number of prerequisite for course i

        for crs, pre in prerequisites:
            preToCrs[pre].append(crs)
            indegree[crs] += 1
        
        # Find all courses with no prerequisite.
        q = collections.deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        
        # Start finishing courses without prerequisite, and update the number of prerequisite.
        res = []
        while q:
            pre = q.popleft()
            res.append(pre)
            for crs in preToCrs[pre]:
                indegree[crs] -= 1
                
                # Append courses without prerequisites.
                if indegree[crs] == 0:
                    q.append(crs)

        return res if len(res) == numCourses else []
