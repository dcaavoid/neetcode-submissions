class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Adjacency list + shortest path with BFS
        # cat -> bat -> bag -> sag
        # *at: {cat, bat}
        # ba*: {bat, bag}
        # *ag: {bag, sag}
        # cat
        # Special case:
        if endWord not in wordList:
            return 0
        
        adj = {}    # pattern: [list of words with this pattern]
        wordList.append(beginWord)
        for s in wordList:
            for i in range(len(s)):
                pattern = s[:i] + "*" + s[i+1:]
                if pattern not in adj:
                    adj[pattern] = []
                adj[pattern].append(s)
        
        q = collections.deque([beginWord])
        visited = set([beginWord])
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res += 1
        
        return 0