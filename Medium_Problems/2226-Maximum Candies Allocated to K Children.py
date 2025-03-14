from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 1, max(candies)
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            total = 0
            
            for pile in candies:
                total += pile // mid
            
            if total >= k:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result
