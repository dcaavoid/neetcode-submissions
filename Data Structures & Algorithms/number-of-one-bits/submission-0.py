class Solution:
    def hammingWeight(self, n: int) -> int:
        # Version 1: check each digit
        res = 0
        while n:
            res += n % 2
            n = n // 2
        return res