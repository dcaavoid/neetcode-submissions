class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Optimzed with iterative DP
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # Gap between l - 1 and r + 1
        for length in range(2, n):
            for l in range(1, n - length + 1):
                r = l + length - 2
                for i in range(l, r + 1):
                    coins = nums[l - 1] * nums[i] * nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)
        
        return dp[1][n - 2]



        # 2D DP where dp[l][r] = max coins given l and r boundary in nums
        # Problem: the number of recursive function calls are too huge.
        # nums = [1] + nums + [1]
        # dp = {}   # key=(l, r), value=max coins

        # def dfs(l, r):
        #     # Base case
        #     if l > r:
        #         return 0
        #     if (l, r) in dp:
        #         return dp[(l, r)]

        #     # Recursive: choose each i in the bound as the LAST to burst
        #     dp[(l, r)] = 0
        #     for i in range(l, r + 1):
        #         coins = nums[l - 1] * nums[i] * nums[r + 1]
        #         coins += dfs(l, i - 1) + dfs(i + 1, r)
        #         dp[(l, r)] = max(dp[(l, r)], coins)
            
        #     return dp[(l, r)]
        
        # return dfs(1, len(nums) - 2)

        # Brute force: backtrack: pick any one of the remaining balloons to burst next
        # Time: O(N!)
        # n = len(nums)
        # alive = set(i for i in range(n))   # Index of alive balloon in nums
        # best = 0

        # # Find the nearest balloon on the left and right of index i.
        # def nearestLeft(i):
        #     j = i - 1
        #     while j >= 0 and j not in alive:
        #         j -= 1
        #     return nums[j] if j >= 0 else 1
        
        # def nearestRight(i):
        #     j = i + 1
        #     while j < n and j not in alive:
        #         j += 1
        #     return nums[j] if j < n else 1

        # def backtrack(curr):
        #     nonlocal best
        #     # Base case: no more balloon
        #     if len(alive) == 0:
        #         best = max(best, curr)
        #         return
            
        #     # Recursive: try to pick each remaining balloon
        #     for i in list(alive):
        #         left = nearestLeft(i)
        #         right = nearestRight(i)
        #         gain = left * nums[i] * right

        #         alive.remove(i)
        #         backtrack(curr + gain)
        #         alive.add(i)
        
        # backtrack(0)
        # return best