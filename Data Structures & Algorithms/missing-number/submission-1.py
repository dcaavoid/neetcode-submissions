class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Version 1: bit manipulation with XOR
        # Doing XOR btwn two same numbers gets 0, and doing XOR btwn 0 and any number gets the number again.
        # The order or logic operation doesn't matter.
        # bit = len(nums)
        
        # for i in range(len(nums)):
        #     bit = bit ^ i ^ nums[i]
        
        # return bit


        # Version 2: difference in sum is the missing number.
        # Time: O(2*n) ~ O(n), space: O(1)
        res = len(nums)
        
        for n in range(len(nums)):
            res += (n - nums[n])
        
        return res