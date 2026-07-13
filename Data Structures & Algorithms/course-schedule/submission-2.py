class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adjacency List (Hash Map) + DFS/BFS
        # Version 1: DFS
        # prereqMap = {i: [] for i in range(numCourses)}  # i: list of prerequisites for i.
        # visited = set()   # courses that are currently waiting for prerequsite to be finished.
        # for crs, pre in prerequisites:
        #     prereqMap[crs].append(pre)
        
        # # Return whether crs can be finished.
        # def dfs(crs: int) -> bool:
        #     # Base case
        #     # 1. No prerequisite
        #     if prereqMap[crs] == []:
        #         return True
        #     # 2. Cycle in prerequisite.
        #     if crs in visited:
        #         return False
            
        #     # Recursively if crs's prerequisites can be finished.
        #     visited.add(crs)
        #     for pre in prereqMap[crs]:
        #         if not dfs(pre):
        #             return False
            
        #     prereqMap[crs] = []
        #     visited.remove(crs)
        #     return True
        
        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False

        # return True

        # -------------------------------------------------------------------------------------
        # Version 2: BFS: start from courses without any prerequsites; and update number of prerequisites.
        preToCrs = {i: [] for i in range(numCourses)}   # prerequisite: list of courses that need this prerequisite.
        indegree = [0] * numCourses    # Number of prereq needed for course i.
        q = collections.deque()   # Track courses that can be taken currently.

        for crs, pre in prerequisites:
            preToCrs[pre].append(crs)
            indegree[crs] += 1
        
        # Start the queue with courses without any prereq.
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        finished = 0
        while q:
            pre = q.popleft()
            finished += 1
            for crs in preToCrs[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)
        
        return finished == numCourses

        