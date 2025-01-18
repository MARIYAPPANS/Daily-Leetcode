from collections import deque

class Solution(object):
    def minCost(self, g):
        m, n = len(g), len(g[0])
        c = [[float('inf')] * n for _ in range(m)]
        c[0][0] = 0
        q = deque([(0, 0)])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            r, cl = q.popleft()
            for i, (dr, dc) in enumerate(d):
                nr, nc = r + dr, cl + dc
                ct = 1 if g[r][cl] != i + 1 else 0
                if 0 <= nr < m and 0 <= nc < n and c[r][cl] + ct < c[nr][nc]:
                    c[nr][nc] = c[r][cl] + ct
                    q.append((nr, nc)) if ct else q.appendleft((nr, nc))
        return c[m - 1][n - 1]
