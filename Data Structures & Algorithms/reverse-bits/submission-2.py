class Solution:
    def reverseBits(self, n: int) -> int:
        # Version 2: %2 and //2
        res = 0
        for i in range(32):
            bit = n % 2     # last bit
            n = n // 2      # Shift to the next bit on the left
            res = res * 2 + bit     # Shift current bits in res to the left by one
        
        return res

        # Version 1: bit shift
        # Start n from last bit and shift to the left;
        # Perform logic AND with the first bit in res.
        # res = 0
        # for i in range(32):
        #     bit = (n >> i) & 1    # Get last bit
        #     res = res | (bit << (31 - i))   # Shift the last i bit to 31-i (front).
        
        # return res