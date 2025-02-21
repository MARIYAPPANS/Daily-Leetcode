class Solution(object):
    def checkIfPrerequisite(self, n, prereq, queries):
        from collections import defaultdict, deque
        g = defaultdict(list)
        p_set = [set() for _ in range(n)]
        for u, v in prereq:
            g[u].append(v)
        for i in range(n):
            q = deque([i])
            while q:
                c = q.popleft()
                for nbr in g[c]:
                    if nbr not in p_set[i]:
                        p_set[i].add(nbr)
                        q.append(nbr)
        return [v in p_set[u] for u, v in queries]
