class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        c = s = 0
        for i in range(n):
            res[i] += s
            c += int(boxes[i])
            s += c
        c = s = 0
        for i in range(n - 1, -1, -1):
            res[i] += s
            c += int(boxes[i])
            s += c
        return res
