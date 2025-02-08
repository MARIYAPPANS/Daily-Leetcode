from collections import Counter, deque

class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        chars = sorted(cnt.items(), key=lambda x: -x[1])
        
        if chars[0][1] > (len(s) + 1) // 2:
            return ""
        
        q = deque()
        for c, f in chars:
            q.extend([c] * f)
        
        res = [''] * len(s)
        idx = 0
        
        for c in q:
            res[idx] = c
            idx += 2
            if idx >= len(s):
                idx = 1
        
        return ''.join(res)
