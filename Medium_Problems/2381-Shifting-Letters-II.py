class Solution:
    def shiftingLetters(self, s: str, sh: List[List[int]]) -> str:
        n = len(s)
        arr = [0] * (n + 1)
        for st, e, d in sh:
            arr[st] += 1 if d == 1 else -1
            arr[e + 1] -= 1 if d == 1 else -1

        for i in range(1, n):
            arr[i] += arr[i - 1]

        res = []
        for i in range(n):
            res.append(chr((ord(s[i]) - ord('a') + arr[i]) % 26 + ord('a')))

        return ''.join(res)
