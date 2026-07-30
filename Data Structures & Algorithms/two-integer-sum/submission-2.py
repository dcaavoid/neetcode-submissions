class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map: number: index
        mapping = {}
        for i, n in enumerate(nums):
            if (target - n) in mapping:
                return [mapping[target - n], i]
            
            mapping[n] = i