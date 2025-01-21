class Solution:
    def gridGame(self, g: List[List[int]]) -> int:
        n = len(g[0])
        top = sum(g[0])
        bot = 0
        res = float('inf')

        for i in range(n):
            top -= g[0][i]
            res = min(res, max(top, bot))
            bot += g[1][i]

        return res
