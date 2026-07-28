class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor: one or the other, but not both
        # 3: 011
        # 2: 010
        # 3: 011
        # If each number n appears exactly twice, n xor n = 0
        # How to convert into bit?
        res = 0
        for n in nums:
            res = res ^ n
        
        return res