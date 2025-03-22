from typing import List
from collections import defaultdict, deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        vis = [False] * n
        cnt = 0
        
        def is_complete(nodes):
            k = len(nodes)
            req = k * (k - 1) // 2
            act = sum(len(g[node]) for node in nodes) // 2
            return act == req
        
        for i in range(n):
            if not vis[i]:
                q = deque()
                q.append(i)
                vis[i] = True
                comp = []
                
                while q:
                    node = q.popleft()
                    comp.append(node)
                    for neighbor in g[node]:
                        if not vis[neighbor]:
                            vis[neighbor] = True
                            q.append(neighbor)
                
                if is_complete(comp):
                    cnt += 1
        
        return cnt
