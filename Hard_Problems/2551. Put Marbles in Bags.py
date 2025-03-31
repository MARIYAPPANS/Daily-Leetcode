from typing import List

class Solution:
    def putMarbles(self, w: List[int], k: int) -> int:
        if k == 1 or len(w) == k:
            return 0
        s = sorted(w[i] + w[i + 1] for i in range(len(w) - 1))
        return sum(s[-(k-1):]) - sum(s[:k-1])
