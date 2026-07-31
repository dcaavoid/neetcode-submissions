class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force: for each number, iterate through the array to except current num.
        # Time: O(n^2), space: O(n)
        #   [1, 2, 4, 6]
        # Optimal: compute the prefix and postfix product for each num.
        # Time: O(3*n) ~ O(n), space: O(n)
        # nums = [1, 3, 0, 6]
        # pre  = [1, 1, 3, 0]
        # post = [0, 0, 6, 1]
        # res  = []
        # pre[i] = pre[i - 1] * nums[i - 1] for i in range(1, len(nums))
        # post[i] = post[i + 1] * nums[i + 1] 
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        res = [0] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        
        return res
