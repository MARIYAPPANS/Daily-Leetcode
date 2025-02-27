from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        idx, dp, res = {x: i for i, x in enumerate(arr)}, {}, 0
        for k, z in enumerate(arr):
            for j in range(k):
                i = idx.get(z - arr[j])
                if i is not None and i < j:
                    dp[j, k] = dp.get((i, j), 2) + 1
                    res = max(res, dp[j, k])
        return res if res > 2 else 0
