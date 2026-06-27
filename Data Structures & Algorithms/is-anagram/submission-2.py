class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Since there are only 26 letters,
        # create a list of 26 to trach the occurence of each letter.
        letters = [0] * 26

        for c in s:
            letters[ord(c) - ord("a")] += 1

        for c in t:
            idx = ord(c) - ord("a")
            letters[idx] -= 1
        
        for num in letters:
            if num != 0:
                return False
        
        return True
        

