class Solution:
    def countServers(self, g):
        r, c = len(g), len(g[0])
        rc, cc = [0] * r, [0] * c

        for i, row in enumerate(g):
            for j, cell in enumerate(row):
                if cell: 
                    rc[i] += 1
                    cc[j] += 1

        return sum(cell for i, row in enumerate(g) for j, cell in enumerate(row) if cell and (rc[i] > 1 or cc[j] > 1))