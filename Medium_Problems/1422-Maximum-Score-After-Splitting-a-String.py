class Solution:
    def maxScore(self, s: str) -> int:
        l, r, max_s = 0, s.count('1'), 0
        
        for i in range(len(s) - 1):
            if s[i] == '0':
                l += 1
            else:
                r -= 1
            
            max_s = max(max_s, l + r)
        
        return max_s
