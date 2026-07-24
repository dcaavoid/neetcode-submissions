class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Cut the string at each position and check if each piece is a palindrome.
        # Use backtrack to cut at every position and undo.
        res = []
        curr = []

        # Given s[:i] is palidrome, parition suffix s[i:] into palidromes.
        def backtrack(i):
            # Base case
            if i == len(s):
                res.append(curr.copy())
                return
            
            # Recursive
            for j in range(i, len(s)):
                if isPali(s, i, j):
                    curr.append(s[i:j+1])
                    backtrack(j + 1)
                    curr.pop()
    
        def isPali(s: str, l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        backtrack(0)
        return res


