class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        rc, cc = [0] * r, [0] * c
        pos = {}

        for i in range(r):
            for j in range(c):
                pos[mat[i][j]] = (i, j)

        for k, v in enumerate(arr):
            x, y = pos[v]
            rc[x] += 1
            cc[y] += 1

            if rc[x] == c or cc[y] == r:
                return k

        return -1
