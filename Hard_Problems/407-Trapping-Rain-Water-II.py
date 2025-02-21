from heapq import heappush, heappop

class Solution:
    def trapRainWater(self, h: List[List[int]]) -> int:
        if not h or not h[0]:
            return 0

        r, c = len(h), len(h[0])
        v = [[False] * c for _ in range(r)]
        hp = []
        
        for i in range(r):
            for j in range(c):
                if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                    heappush(hp, (h[i][j], i, j))
                    v[i][j] = True

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        w = 0

        while hp:
            ht, x, y = heappop(hp)
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and not v[nx][ny]:
                    w += max(0, ht - h[nx][ny])
                    heappush(hp, (max(ht, h[nx][ny]), nx, ny))
                    v[nx][ny] = True

        return w
