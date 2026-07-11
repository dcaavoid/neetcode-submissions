class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Backtracking
        digitToChar = {'2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz'}
        
        res = []

        # Return the letters up until index i in digits.
        def backtrack(i: int, curr: str):
            # Base case
            if i == len(digits):
                res.append(curr)
                return
            
            # Recursive
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curr + c)
        
        # Return emtpy list if digits is null.
        if digits:
            backtrack(0, "")
        
        return res