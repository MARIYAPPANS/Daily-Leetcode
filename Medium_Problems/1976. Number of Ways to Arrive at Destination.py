from heapq import heappush, heappop
from collections import defaultdict
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        g = defaultdict(list)
        for u, v, t in roads:
            g[u].append((v, t))
            g[v].append((u, t))
        
        d = [float('inf')] * n
        d[0] = 0
        w = [0] * n
        w[0] = 1
        pq = [(0, 0)]
        
        while pq:
            ct, u = heappop(pq)
            if ct > d[u]:
                continue
            for v, t in g[u]:
                nt = ct + t
                if nt < d[v]:
                    d[v] = nt
                    w[v] = w[u]
                    heappush(pq, (nt, v))
                elif nt == d[v]:
                    w[v] = (w[v] + w[u]) % MOD
        
        return w[n - 1] % MOD
