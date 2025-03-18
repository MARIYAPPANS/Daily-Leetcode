from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ml = 0
        l = 0
        bm = 0
        
        for r in range(len(nums)):
            while bm & nums[r]:
                bm ^= nums[l]
                l += 1
            
            bm |= nums[r]
            ml = max(ml, r - l + 1)
        
        return ml
