class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Initial thought: sliding window, if left pointer in s2 exists in s1, move right pointer after left pointer.
        # Fixed length window: Since we are looking for permutations of s1, len(s1) = len(substring(s2))
        # Problem: how to resolve the number of occurence for each letter?
        # Answer: use array of length 26.
        if len(s1) > len(s2):
            return False
        
        # Since both strings only contain lowercase letters, use array to count the occurence of each letter.
        s1Count = [0] * 26
        s2Count = [0] * 26
        base = ord("a")

        # Initialize the count of s1 and s2            
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - base] += 1
            s2Count[ord(s2[i]) - base] += 1
        
        # matches = how many characters match in occurence
        # In the following sliding windoe ,for comparing matches, there are three cases:
        # (1) If was unequal, now equal: matches += 1
        # (2) If was equal, now not equal: match -= 1
        # (If) If was unequal, now still not equal: match stays
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        # Initialize pointers and move the fixed length window
        left = 0

        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # Add the character from s2 at the right pointer
            index = ord(s2[right]) - base
            s2Count[index] += 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] - 1 == s1Count[index]:
                matches -= 1
            
            # Remove the character from s2 at the left pointer
            index = ord(s2[left]) - base
            s2Count[index] -= 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] + 1 == s1Count[index]:
                matches -= 1
            left += 1
        
        return matches == 26
