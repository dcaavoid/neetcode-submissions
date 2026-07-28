class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # p[i] = [a, b] <=> b->a
        # detect cycle
        # 1. DFS: build a map(course: [list of prerequisites]), a visited set, and a finished set.
        #    for each course, finish all the prereq recursively;
        #    if a course has no prereq, return true;
        #    use a set to track the visited courses along the current dfs path, and if any duplicate exists, return false;
        # Given V = # of courses, E = # number of prereq, time: O(V+E), space: O(V+E)
        # adj = {n: [] for n in range(numCourses)}    # course: list of prereq
        # for crs, prereq in prerequisites:
        #     adj[crs].append(prereq)

        # visited = set()

        # def dfs(c: int) -> bool:
        #     # Base case
        #     # 1. Cycle in the dfs path, prereq cannot be finished
        #     if c in visited:
        #         return False
        #     # 2. This course has no prereq.
        #     if not adj[c]:
        #         return True
            
        #     # Recursive: finish all prereq using dfs.
        #     visited.add(c)
        #     for nei in adj[c]:
        #         if not dfs(nei):
        #             return False
            
        #     adj[c] = []
        #     visited.remove(c)
        #     return True
                

        # for c in range(numCourses):
        #     if not dfs(c):
        #         return False
        
        # return True

        # ---------------------------------------------------------------------------------------
        # 2: BFS: build a map (prereq: list of courses) and a list to count the number of prereq;
        #    If a course has no prereq now, add to queue
        # But how to track visited along the BFS -> no need b/c a course stuck in the cycle can never reach # of prereq = 0.
        prereqToCourse = {c: [] for c in range(numCourses)}   # prereq: [list of courses]
        indegree = [0] * numCourses     # indegree[i] = number of prereqs for course i
        for crs, prereq in prerequisites:
            prereqToCourse[prereq].append(crs)
            indegree[crs] += 1
        
        # Add courses without prereq to the queue.
        q = collections.deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        
        # For each prereq, update the indegree of its dependent courses.
        finished = 0
        while q:
            prereq = q.popleft()
            for c in prereqToCourse[prereq]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
            finished += 1
        
        return finished == numCourses