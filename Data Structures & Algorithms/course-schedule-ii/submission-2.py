class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Version 2: BFS with kahn's algo (track indegree)
        adj = { n: [] for n in range(numCourses) }  # prereq: [list of courses with this prereq]
        indegree = [0] * numCourses     # indegree[i] = number of prereqs for course i
        res = []    # topological order of courses
        for c, p in prerequisites:
            adj[p].append(c)
            indegree[c] += 1
        
        q = collections.deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
                res.append(c)
        
        while q:
            c = q.popleft()
            for n in adj[c]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
                    res.append(n)
        
        return res if len(res) == numCourses else []

        # -----------------------------------------------------------------------------
        # Valid ordering = topological sort
        # Version 1: DFS in post-order
        # Time: O(V+E), space: O(V+E)
        # adj = {n: [] for n in range(numCourses)}    # course: [list of prerequisites]
        # for c, p in prerequisites:
        #     adj[c].append(p)
        
        # visited = set()
        # finished = set()
        # res = []

        # # Return if course c and all its prereq can be finished
        # def dfs(c: int) -> bool:
        #     # Base case
        #     if c in visited:
        #         return False
        #     if c in finished:
        #         return True
            
        #     # Recursive
        #     visited.add(c)
        #     for n in adj[c]:
        #         if not dfs(n):
        #             return False
            
        #     visited.remove(c)
        #     finished.add(c)
        #     res.append(c)
        #     return True

        # for c in range(numCourses):
        #     if not dfs(c):
        #         return []
        
        # return res