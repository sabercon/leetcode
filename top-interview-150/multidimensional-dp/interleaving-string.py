class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [True] * (len(s2) + 1)
        for j, c2 in enumerate(s2):
            dp[j + 1] = dp[j] and c2 == s3[j]
        for i, c1 in enumerate(s1):
            dp[0] = dp[0] and c1 == s3[i]
            for j, c2 in enumerate(s2):
                dp[j + 1] = (dp[j] and c2 == s3[i + j + 1]) or (dp[j + 1] and c1 == s3[i + j + 1])
        return dp[-1]
