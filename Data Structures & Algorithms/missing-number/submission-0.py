class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Version 1: bit manipulation with XOR
        # Doing XOR btwn two same numbers gets 0, and doing XOR btwn 0 and any number gets the number again.
        # The order or logic operation doesn't matter.
        bit1, bit2 = 0, 0
        for n in nums:
            bit1 = bit1 ^ n
        
        for n in range(len(nums) + 1):
            bit2 = bit2 ^ n
        
        return bit1 ^ bit2


        # Version 2: difference in sum is the missing number.
        # Time: O(2*n) ~ O(n), space: O(1)
        # sum1, sum2 = 0, 0
        # for n in nums:
        #     sum1 += n
        
        # for n in range(len(nums) + 1):
        #     sum2 += n
        
        # return sum2 - sum1