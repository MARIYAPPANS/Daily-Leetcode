from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat = [cell for row in grid for cell in row]
        flat.sort()
        
        remainder = flat[0] % x
        for num in flat:
            if num % x != remainder:
                return -1
        
        n = len(flat)
        median = flat[n // 2]
        
        operations = 0
        for num in flat:
            operations += abs(num - median) // x
        
        return operations
