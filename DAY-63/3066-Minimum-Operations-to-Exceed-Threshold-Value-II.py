from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        operations = 0
        
        while nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            heappush(nums, x * 2 + y)
            operations += 1
        
        return operations
