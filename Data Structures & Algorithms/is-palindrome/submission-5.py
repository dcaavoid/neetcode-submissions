class Solution:
    # Return True if c is a alphanumeric character
    def alphaNum(self, c: str) -> bool:
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))

    def isPalindrome(self, s: str) -> bool:
        # Two pointers
        # Remove alphanumeric characters (space, punctuation)
        # Convert all letters into lower case.
        # Time: O(n), space: O(1)
        left, right = 0, len(s) - 1
        while left < right:
            # Remove space at each pointer
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while left < right and not self.alphaNum(s[right]):
                right -= 1
            
            # Compare letters in lower case
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True

