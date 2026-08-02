class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # For each number i in nums that i - 1 not in nums,
        # build sequence until i + 1 not in nums.
        # For O(1) retrieval, use hash set.
        # Time: O(n), space: O(n)
        nums = set(nums)
        longest = 0
        for n in nums:
            # Skip if n is not a starting number in a sequence.
            if n - 1 in nums:
                continue
            
            curr = 1
            while n + curr in nums:
                curr += 1
            
            longest = max(curr, longest)
        
        return longest
