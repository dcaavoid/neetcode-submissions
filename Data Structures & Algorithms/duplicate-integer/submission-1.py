class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = list(set(nums))
        return len(nums) != len(unique_nums)
            
