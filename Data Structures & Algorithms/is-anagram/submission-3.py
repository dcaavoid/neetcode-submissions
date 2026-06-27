class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Since there are only 26 letters,
        # create a list of 26 to trach the occurence of each letter.
        # First check if two strings are equal in length
        if len(s) != len(t):
            return False

        letters = [0] * 26
        base = ord("a")

        for c in s:
            letters[ord(c) - base] += 1

        for c in t:
            idx = ord(c) - base
            letters[idx] -= 1
        
        for num in letters:
            if num != 0:
                return False
        
        return True
        

