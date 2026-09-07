class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        MOD = 10 ** 9 + 7
        n, m = len(s), len(t)
        if m > n:
            return 0

        dp = [1] + [0] * m  # dp[j] = ways to form t[:j] using s[:i] so far
        for i in range(1, n + 1):
            # iterate j backwards so dp[j-1] is still the value from row i-1
            for j in range(min(i, m), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] = (dp[j] + dp[j - 1]) % MOD
        return dp[m]