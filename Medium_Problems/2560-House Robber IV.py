from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = min(nums), max(nums)
        while l < r:
            m = (l + r) // 2
            take, skip = 0, True
            for n in nums:
                if skip and n <= m:
                    take += 1
                    skip = False
                else:
                    skip = True
            if take >= k:
                r = m
            else:
                l = m + 1
        return l
