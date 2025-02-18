class Solution:
    def smallestNumber(self, pattern: str) -> str:
        s, r = [], []
        for i, c in enumerate(pattern + 'I', 1):
            s.append(str(i))
            if c == 'I':
                r += s[::-1]
                s = []
        return ''.join(r)
