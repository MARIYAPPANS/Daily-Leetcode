from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, dirs = len(grid), [(0,1), (1,0), (0,-1), (-1,0)]
        d, res, idx = {}, 0, 2

        def dfs(x, y, idx):
            s = 1
            grid[x][y] = idx
            for dx, dy in dirs:
                i, j = x + dx, y + dy
                if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                    s += dfs(i, j, idx)
            return s

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    d[idx] = dfs(i, j, idx)
                    res = max(res, d[idx])
                    idx += 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen, s = set(), 1
                    for dx, dy in dirs:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] > 1:
                            seen.add(grid[x][y])
                    for k in seen:
                        s += d[k]
                    res = max(res, s)

        return res if res else n * n
