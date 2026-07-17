class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. Dynamic programming: bottom-up
        # dp = [float('inf')] * (amount + 1)
        # dp[0] = 0

        # for a in range(1, amount + 1, 1):
        #     for c in coins:
        #         if a - c >= 0:
        #             dp[a] = min(dp[a], 1 + dp[a - c])
        
        # return dp[amount] if dp[amount] != float('inf') else -1

        # 2. BFS
        if amount == 0:
            return 0
        
        visited = set([0])
        q = collections.deque([0])
        step = 0

        while q:
            step += 1
            for _ in range(len(q)):
                curr = q.popleft()
                for c in coins:
                    nxt = curr + c
                    if nxt == amount:
                        return step
                    
                    if nxt < amount and nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
        
        return -1