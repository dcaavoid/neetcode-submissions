class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use hash map: char: number of occurrence.
        # Can be optimized further to use array.
        # First pass, build the array;
        # Second pass, check the occurrence of each letter.
        if len(s) != len(t):
            return False
        
        letters = [0] * 26
        base = ord('a')
        for i in range(len(s)):
            letters[ord(s[i]) - base] += 1
            letters[ord(t[i]) - base] -= 1
        
        for n in letters:
            if n != 0:
                return False
        
        return True
        
