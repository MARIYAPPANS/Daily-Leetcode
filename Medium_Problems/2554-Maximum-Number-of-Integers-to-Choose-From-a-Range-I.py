class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        total_sum = 0
        count = 0
        
        for i in range(1, n + 1):
            if i not in banned:
                if total_sum + i > maxSum:
                    break
                total_sum += i
                count += 1
        
        return count
