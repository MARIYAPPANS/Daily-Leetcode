from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:  
            return 1  # Edge case: single element
        
        max_len = inc = dec = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1  # Reset decreasing sequence
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1  # Reset increasing sequence
            else:
                inc = dec = 1  # Reset both

            if max_len < inc:  
                max_len = inc  # Manual max() to reduce function call overhead
            if max_len < dec:  
                max_len = dec  

        return max_len
