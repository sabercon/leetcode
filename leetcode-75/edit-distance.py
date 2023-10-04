class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = list(range(len(word2) + 1))
        for c1 in word1:
            temp = dp.copy()
            temp[0] += 1
            for i, c2 in enumerate(word2):
                if c1 == c2:
                    temp[i + 1] = dp[i]
                else:
                    temp[i + 1] = min(temp[i], dp[i], dp[i + 1]) + 1
            dp = temp
        return dp[-1]
