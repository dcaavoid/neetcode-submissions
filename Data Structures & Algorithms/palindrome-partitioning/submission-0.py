class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Backtracking
        res = []
        curr = []

        # Generate all the palindrome after index i in s.
        def dfs(i):
            # Base case: no more palidromes after s[i].
            if i == len(s):
                res.append(curr.copy())
                return
            
            # Recursive: try every possible slicing j in s[i:len(s)].
            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    curr.append(s[i:j+1])
                    dfs(j + 1)
                    curr.pop()
        
        dfs(0)
        return res
    
    def isPalin(self, s: str, left: int, right: int) -> bool:
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True