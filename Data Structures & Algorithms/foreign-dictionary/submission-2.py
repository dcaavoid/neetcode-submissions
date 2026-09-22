class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Topological sort (DFS in post-order)
        # Build adjacency list for every character: char: set(chars) with higher order
        adj = { c: set() for w in words for c in w }

        # Compare each pair of word
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            # Invalid if the shorter word appears after its prefix
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            # Find first differing char and add to the adjacency list
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}    # char: True if char in current DFS; False if char is fully processed
        res = []    # Save DFS post order result

        # True if c still in current DFS; False if c is fully processed.
        def dfs(c) -> bool:
            # Check status of char c in visited
            if c in visited:
                return visited[c]
            
            visited[c] = True

            for nei in adj[c]:
                # Check if any neighbor chars are in the cycle
                if dfs(nei):
                    return True
                
            # No cycle and save current char into result
            visited[c] = False
            res.append(c)
            return False
        
        # Try every character as the starting point
        for c in adj:
            if dfs(c):
                return ""
        
        # Since post order, reverse the result
        res.reverse()
        return "".join(res)