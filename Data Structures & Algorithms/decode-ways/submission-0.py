class Solution:
    def numDecodings(self, s: str) -> int:
        # Dynamic programming (bottom-up)
        # dp[i]: starting from index i in s, how many ways of valid combinations are there?
        # dp1: if s[i] can be decoded, ways of valid combinations in s[i+1:]
        # dp2: if s[i] and s[i+1] can be decoded together, ways of valid combinatsion in s[i+2:]
        dp1, dp2 = 1, 1

        for i in range(len(s) - 1, -1 , -1):
            # 0 is invalid for single number decoding
            if s[i] == "0":
                curr = 0
            # s[i] is valid for single number decoding
            else:
                curr = dp1
                
                # s[i] + s[i+1] is valid for two-digit decoding
                if (i + 1 < len(s) and
                    (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                    curr += dp2
            
            dp2 = dp1
            dp1 = curr
        
        return dp1

