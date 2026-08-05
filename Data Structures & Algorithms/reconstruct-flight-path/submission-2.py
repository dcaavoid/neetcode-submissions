class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build adjacency list to represent the path.
        # Run DFS starting at JFK.
        # Valid path: len(res) = len(tickets) + 1
        adj = {}
        tickets.sort()
        for f, t in tickets:
            if f not in adj:
                adj[f] = []
            adj[f].append(t)
        
        res = ["JFK"]

        # Return if current source creates a valid path.
        def backtrack(src: str) -> bool:
            # Base case
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            # Recursive
            temp = adj[src]
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)

                if backtrack(v):
                    return True
                
                adj[src].insert(i, v)
                res.pop()
            
            return False
        
        backtrack("JFK")
        return res

        