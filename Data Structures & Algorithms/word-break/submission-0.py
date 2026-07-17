class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP: bottom-up
        # dp[i]: for s[i:], is there a word in wordDict that match?
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # Just need to find one word split for s[i:]
                if dp[i]:
                    break

                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
        
        return dp[0]