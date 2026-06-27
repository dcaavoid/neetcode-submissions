class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # Two pointers: start and end
        # # Problem: how to solve case-insensitive and ignore non-alphanumeric characters?
        # # Answer: use .isalnum()
        # # Problem: how to convert a string with space to a consecutive string?
        # # Answer: work in-place, and skip if there is a space

        # left, right = 0, len(s) - 1

        # while left < right:
        #     # Ignores all non-alphanumeric characters
        #     while ((left < len(s))
        #         and (not s[left].isalnum() or s[left] == " ")):
        #         left += 1
            
        #     while ((right > -1)
        #         and (not s[right].isalnum() or s[right] == " ")):
        #         right -= 1
            
        #     # Compare in case-insensitive
        #     if s[left].lower() != s[right].lower():
        #         return False
            
        #     left += 1
        #     right -= 1
        
        # return True

        # Solution 2: create a new string without any non-alphanumeric characters
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]