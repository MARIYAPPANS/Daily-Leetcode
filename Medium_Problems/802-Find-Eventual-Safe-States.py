class Solution:
    def eventualSafeNodes(self, g: [[int]]) -> [int]:
        n = len(g)
        rg = [[] for _ in range(n)]
        od = [0] * n
        
        for u in range(n):
            for v in g[u]:
                rg[v].append(u)
            od[u] = len(g[u])
        
        q = []
        for i in range(n):
            if od[i] == 0:
                q.append(i)
        
        res = []
        while q:
            x = q.pop(0)
            res.append(x)
            for y in rg[x]:
                od[y] -= 1
                if od[y] == 0:
                    q.append(y)
        
        res.sort()  
        return res
