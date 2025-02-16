from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        m = 2 * n - 1
        res = [0] * m
        used = [False] * (n + 1)

        def backtrack(i):
            if i == m:
                return True
            if res[i] != 0:
                return backtrack(i + 1)
            for v in range(n, 0, -1):
                if not used[v] and (v == 1 or (i + v < m and res[i + v] == 0)):
                    res[i] = v
                    if v > 1:
                        res[i + v] = v
                    used[v] = True
                    if backtrack(i + 1):
                        return True
                    res[i] = 0
                    if v > 1:
                        res[i + v] = 0
                    used[v] = False
            return False

        backtrack(0)
        return res
