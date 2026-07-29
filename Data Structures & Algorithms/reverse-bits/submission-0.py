class Solution:
    def reverseBits(self, n: int) -> int:
        # Start n from last bit and shift to the left;
        # Perform logic AND with the first bit in res.
        res = 0
        for i in range(32):
            bit = (n >> i) & 1    # Get last bit
            res = res | (bit << (31 - i))   # Shift the last i bit to 31-i (front).
        
        return res