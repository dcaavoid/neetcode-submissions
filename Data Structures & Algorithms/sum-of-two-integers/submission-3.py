class Solution:
    def getSum(self, a: int, b: int) -> int:
        # a xor b gives the actual digit of bit in binary:
        # 1 xor 0 = 1, 0 xor 0 = 0, 1 xor 1 = 0
        # a and b << 1 gives the carry to the next bit
        # Python integers have unbounded precision — negative numbers aren't stored in a fixed 32-bit register like in Java/C++. 
        mask = 0xFFFFFFFF   # F in hex = 1111 in binary -> 32 bits
        
        while b != 0:
            xor = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = xor
            b = carry
        
        # If a's 32nd bit (sign bit) is set, convert back to a negative Python int
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)