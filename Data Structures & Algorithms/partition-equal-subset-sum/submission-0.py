class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # In order to be partition, sum(nums) must be even.
        if sum(nums) % 2:
            return False
        
        dp = set([0])
        target = sum(nums) // 2

        for i in range(len(nums)):
            nextDP = set()
            for n in dp:
                nxt = n + nums[i]
                if nxt == target:
                    return True
                nextDP.add(nxt)
                nextDP.add(n)
            dp = nextDP
        
        return False
        