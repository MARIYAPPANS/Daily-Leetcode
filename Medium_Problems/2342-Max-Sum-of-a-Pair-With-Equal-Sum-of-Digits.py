from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ds, max_s = {}, -1
        
        for n in nums:
            s, temp = 0, n
            while temp:  # Compute digit sum without string conversion
                s += temp % 10
                temp //= 10
            
            if s in ds:
                max_s = max_s if max_s > ds[s] + n else ds[s] + n
                ds[s] = ds[s] if ds[s] > n else n
            else:
                ds[s] = n
        
        return max_s
