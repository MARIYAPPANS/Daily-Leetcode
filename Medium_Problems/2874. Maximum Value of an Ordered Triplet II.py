class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max1 = max2 = max_diff = 0
        res = 0
        for x in nums:
            res = max(res, max_diff * x)
            max_diff = max(max_diff, max1 - x)
            max1 = max(max1, x)
        return res
