class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1  # Base case: an empty string is always valid
        mod = 10**9 + 7

        for length in range(1, high + 1):
            if length >= zero:
                dp[length] += dp[length - zero]
            if length >= one:
                dp[length] += dp[length - one]
            dp[length] %= mod

        return sum(dp[low:high + 1]) % mod
