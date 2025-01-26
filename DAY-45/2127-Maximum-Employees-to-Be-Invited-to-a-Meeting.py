class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indeg = [0] * n
        for i in range(n):
            indeg[favorite[i]] += 1
        
        used = [False] * n
        f = [1] * n
        q = deque(i for i in range(n) if indeg[i] == 0)
        
        while q:
            u = q.popleft()
            used[u] = True
            v = favorite[u]
           
            f[v] = max(f[v], f[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
        
       
        ring = total = 0
        for i in range(n):
            if not used[i]:
                j = favorite[i]
                if favorite[j] == i:
                    total += f[i] + f[j]
                    used[i] = used[j] = True
                else:
                    u = i
                    cnt = 0
                    while True:
                        cnt += 1
                        u = favorite[u]
                        used[u] = True
                        if u == i:
                            break
                    ring = max(ring, cnt)
        
        return max(ring, total)