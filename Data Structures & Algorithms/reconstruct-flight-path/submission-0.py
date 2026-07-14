class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Adjacency list + DFS
        tickets.sort()
        adj = {}
        for src, dst in tickets:
            if src not in adj:
                adj[src] = []
            adj[src].append(dst)
        
        res = ['JFK']

        # Return if all tickets can be used starting from
        def dfs(src):
            # Base case
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            # Recursive
            temp = adj[src]
            for i, dst in enumerate(temp):
                adj[src].pop(i)
                res.append(dst)
                if dfs(dst):
                    return True
                adj[src].insert(i, dst)
                res.pop()
            
            return False
        
        dfs('JFK')
        return res