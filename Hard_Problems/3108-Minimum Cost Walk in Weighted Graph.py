class Solution:
    def minimumCost(self, n: int, e: List[List[int]], q: List[List[int]]) -> List[int]:
        p = list(range(n))
        m = [-1] * n

        def f(x: int) -> int:
            if p[x] != x:
                p[x] = f(p[x])
            return p[x]

        for a, b, w in e:
            ra, rb = f(a), f(b)
            m[rb] &= w
            if ra != rb:
                m[rb] &= m[ra]
                p[ra] = rb

        r = []
        for a, b in q:
            if a == b:
                r.append(0)
            elif f(a) != f(b):
                r.append(-1)
            else:
                r.append(m[f(a)])
        return r
