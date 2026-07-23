class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # If word1[i] == word2[j], go to next chars (i + 1, j + 1).
        # If word1[i] != word2[j], there are three possible operations:
        #   1. insert matching char into word1 before i, then go to (i, j + 1);
        #   2. delete word1[i], then go to (i + 1, j);
        #   3. replace word1[i] with matchin char, then go to (i + 1, j + 1)
        # Edge cases:
        #   1. If word1 is emtpy but word2 is not empty, take len(word2) operations;
        #   2. If word1 is not empty but word2 is empty, take len(word1) operations;
        #   3. If both word1 and word2 are emtpy, take 0 operation.
        # Build 2D DP with (len(word1) + 1) * (len(word2) + 1), then bottom up.
        # 
        
        m, n = len(word1), len(word2)
        dp = [float('inf')] * (n + 1)

        for i in range(m, -1, -1):
            newDP = [float('inf')] * (n + 1)
            for j in range(n, -1, -1):
                # Edge case 1: no more word
                if i == m and j == n:
                    newDP[j] = 0
                # Edge case 2: word1 is empty, but word2 is not empty
                elif i == m:
                    newDP[j] = n - j
                # Edge case 3: word2 is empty, but word1 is not empty
                elif j == n:
                    newDP[j] = m - i
                else:
                    if word1[i] == word2[j]:
                        newDP[j] = dp[j + 1]
                    else:
                        insert_op = 1 + newDP[j + 1]
                        delete_op = 1 + dp[j]
                        replace_op = 1 + dp[j + 1]
                        newDP[j] = min(insert_op, delete_op, replace_op)
            
            dp = newDP
        
        return dp[0]
