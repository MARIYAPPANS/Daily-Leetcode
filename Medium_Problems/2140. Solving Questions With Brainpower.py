class Solution:
    def mostPoints(self, q: List[List[int]]) -> int:
        n = len(q)
        dp = [0] * n
        dp[-1] = q[-1][0]
        for i in range(n - 2, -1, -1):
            p, b = q[i]
            dp[i] = max(dp[i + 1], p + (dp[i + b + 1] if i + b + 1 < n else 0))
        return dp[0]
