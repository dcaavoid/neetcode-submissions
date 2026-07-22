class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # DFS with two choices: 1. + current num; 2. - current num;
        # Use hash map
        dp = {}    # key=(index in nums, current sum), value=number of combinations

        # Given current sum a, return number of combinations with nums[i:]
        def dfs(i, a):
            # Base case
            if i == len(nums):
                if a == target:
                    return 1
                else:
                    return 0
            
            if (i, a) in dp:
                return dp[(i, a)]
            
            # Recursive
            dp[(i, a)] = dfs(i + 1, a + nums[i]) + dfs(i + 1, a - nums[i])
            return dp[(i, a)]
        
        dfs(0, 0)
        return dp[(0, 0)]