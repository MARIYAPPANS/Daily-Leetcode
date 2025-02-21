class Solution:
    def lexicographicallySmallestArray(self, a, l):
        b = sorted(a)

        g = 0
        m = {}
        m[b[0]] = g

        d = {}
        d[g] = deque([b[0]])

        for i in range(1, len(a)):
            if abs(b[i] - b[i - 1]) > l:
                g += 1

            m[b[i]] = g

            if g not in d:
                d[g] = deque()
            d[g].append(b[i])

        for i in range(len(a)):
            n = a[i]
            g = m[n]
            a[i] = d[g].popleft()

        return a
