class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute force: for every substring of s2, compare with s1.
        # Time: O(n^2 + n log n)
        if len(s1) > len(s2):
            return False
        
        s1 = "".join(sorted(s1))
        for i in range(len(s2) - len(s1) + 1):
            subseq = "".join(sorted(s2[i:i+len(s1)]))
            if s1 == subseq:
                return True
        
        return False

        # Check permuation: same frequency of letters -> hash map
        # Sliding window