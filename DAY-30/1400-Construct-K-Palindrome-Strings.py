class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        return sum(v % 2 for v in Counter(s).values()) <= k
