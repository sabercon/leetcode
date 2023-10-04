class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)
        for c1 in text1:
            temp_db = [0] * (len(text2) + 1)
            for i, c2 in enumerate(text2):
                if c1 == c2:
                    temp_db[i + 1] = dp[i] + 1
                else:
                    temp_db[i + 1] = max(temp_db[i], dp[i + 1])
            dp = temp_db
        return dp[-1]
