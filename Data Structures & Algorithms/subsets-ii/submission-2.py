class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Two choices at each step: 1. choose current integer and go to next integer; 2. go to next integer
        nums.sort()
        res = []

        # Given index i in nums and current subset, return all subsets.
        def backtrack(i, curr):
            # Base case
            if i == len(nums):
                res.append(curr.copy())
                return
            
            # Recursive
            # 1. choose current number
            curr.append(nums[i])
            backtrack(i + 1, curr)

            # 2. skip all duplicates
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, curr)
        
        backtrack(0, [])
        return res