class Solution:
    def hammingWeight(self, n: int) -> int:
        # Version 2: Brian Kernighan's trick
        # Time: O(a) where a = number of 1s
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res

        # Version 1: check each digit
        # Time: O(32) ~ O(1)
        # res = 0
        # while n:
        #     res += n % 2
        #     n = n // 2
        # return res