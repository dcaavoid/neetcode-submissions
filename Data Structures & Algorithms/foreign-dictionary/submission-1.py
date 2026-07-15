class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Topological Sort + DFS/BFS
        # Version 1. DFS in post-order to return True if the current path has cycle:
        # 1. Not visited yet; 2. visited[c] = True: has cycle; 3. visited[c] = False: done visiting.
        # Build adjacency list: c1: c2 (c1 must comes before c2)
        adj = { c: set() for word in words for c in word }
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # Check if the order is invalid
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            # Add order of letter
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        # Three states for each character:
        # 1. not visited; 2. visited[c] = False, safe to choose;
        # 3. visited[c] = True, still in current recursion, has cycle.
        visited = {}
        res = []    # Save characters in post order (reversed)

        # Return True if there is cycle starting from character c.
        def dfs(c):
            # Base case
            if c in visited:
                return visited[c]
            
            # Recursive in post order
            visited[c] = True   # In recursion
            for nei in adj[c]:
                if dfs(nei):
                    return True
            
            visited[c] = False  # Safe without cycle
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
