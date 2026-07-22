class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Version 2: DP (bottom up)
        # dp[i][j] = True if suffix i of s1 and j of s2 can come up with suffix i+j of s3.
        # s3 = a a b b b b a a
        #   b b b b 0  s2 = j
        # a
        # a
        # a
        # a
        # 0       F T
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [False] * (len(s2) + 1)

        for i in range(len(s1), -1, -1):
            newDP = [False] * (len(s2) + 1)
            for j in range(len(s2), -1, -1):
                # Base case
                if i == len(s1) and j == len(s2):
                    newDP[j] = True
                    continue
                
                # Choose the current char from s1,
                # and then check suffix i+1 of s1 and j of s2 can come up with suffix i+j+1 of s3.
                s1_term = i < len(s1) and s1[i] == s3[i+j] and dp[j]

                # Choose the current char from s2,
                # and then check suffix i of s1 and j+1 of s2 can come up with suffix i+j+1 of s3.
                s2_term = j < len(s2) and s2[j] == s3[i+j] and newDP[j+1]

                newDP[j] = s1_term or s2_term

            dp = newDP
        
        return dp[0]
                

        # Verion 1: backtrack: if s1[i+1]=s2[j]=s3[i+j], there are two choices:
        # 1. s3[i+j] is from s1[i]; 2. s3[i+j] is from s2[j].
        # dfs(i, j): after using first i's chars from s1 and first j's chars from s2,
        #            return if first (i+j)'s chars in s3 can be interleaved.
        # Time: O(2^(m+n)) b/c state (i, j) will divide into (i+1, j) and (i, j+1);
        # Space: O(M+N)
        # def dfs(i, j):
        #     k = i + j
        #     # Base case
        #     if i + j == len(s3):
        #         return True
            
        #     # Recursive
        #     # 1. Next char in s3 is from s1
        #     if i < len(s1) and s1[i] == s3[k]:
        #         if dfs(i + 1, j):
        #             return True
            
        #     # 2. Next char in s3 is from s2
        #     if j < len(s2) and s2[j] == s3[k]:
        #         if dfs(i, j + 1):
        #             return True
            
        #     return False
        
        # return dfs(0, 0)