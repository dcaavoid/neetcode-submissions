class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Optimal solution: fixed-size sliding window
        # Instead of comparing all the values as the window updates, create a variable to track the number of matched frequencies in both.
        # Time: O(26 + n) ~ O(n), space: O(26) ~ O(1) as only lower case chars.
        if len(s1) > len(s2):
            return False
        
        # Build frequencies of first len(s1) subsequence
        s1Count = [0] * 26
        s2Count = [0] * 26
        base = ord('a')
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - base] += 1
            s2Count[ord(s2[i]) - base] += 1
        
        # Initial check of matches
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0
        
        # Sliding window with fixed size
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # Add letter at the right pointer
            index = ord(s2[right]) - base
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            # Only decrement matches if the frequency doesn't match for the first time
            elif s1Count[index] == s2Count[index] - 1:
                matches -= 1
            
            # Remove letter at the left pointer
            index = ord(s2[left]) - base
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            # Only decrement matches if the frequency doesn't match for the first time
            elif s1Count[index] == s2Count[index] + 1:
                matches -= 1

            left += 1
        
        return matches == 26


        # Brute force: for every substring of s2, compare with s1.
        # Time: O(n^2 + n log n)
        # if len(s1) > len(s2):
        #     return False
        
        # s1 = "".join(sorted(s1))
        # for i in range(len(s2) - len(s1) + 1):
        #     subseq = "".join(sorted(s2[i:i+len(s1)]))
        #     if s1 == subseq:
        #         return True
        
        # return False