from collections import Counter
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(target), len(words[0])
        dp = [0] * (m + 1)
        dp[0] = 1

        char_count = [Counter(col) for col in zip(*words)]
        
        for j in range(n):
            for i in range(m - 1, -1, -1):
                dp[i + 1] += dp[i] * char_count[j][target[i]]
                dp[i + 1] %= MOD

        return dp[m]
