class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use hash map: char: number of occurrence.
        # First pass, build the hash map;
        # Second pass, check the occurrence of each letter.
        if len(s) != len(t):
            return False
        
        charCount= {i: 0 for i in range(26)}
        for i in range(len(s)):
            charCount[ord(s[i]) - ord('a')] += 1
            charCount[ord(t[i]) - ord('a')] -= 1
        
        for _, val in charCount.items():
            if val != 0:
                return False
        
        return True
        
