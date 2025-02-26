class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s, mx, mn = 0, 0, 0
        for n in nums:
            s += n
            mx = max(mx, s)
            mn = min(mn, s)
        return mx - mn
