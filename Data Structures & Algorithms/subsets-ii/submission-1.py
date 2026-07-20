class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Since we don't want duplicate subset, we need to sort the input array first.
        # Use backtracking with two paths:
        # 1. Use the current element and then recursively build subset starting from next element;
        # 2. Do not use the current element and skip any following duplicate elements.
        res = []
        nums.sort()

        # Append nums[i] into to current subset, and then append current subset into res.
        def backtrack(i, subset):
            # Base case
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # Recursive
            # 1. Subset with nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # 2. Subset without any nums[i] by skipping duplicate numbers
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        return res
