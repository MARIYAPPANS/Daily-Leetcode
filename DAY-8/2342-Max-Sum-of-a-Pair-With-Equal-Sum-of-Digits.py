class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        new = {}
        max_sum = -1
        for num in nums:
            digit_sum = sum(int(j) for j in str(num))
            if digit_sum in new:
                max_sum = max(max_sum, new[digit_sum] + num)
            new[digit_sum] = max(new.get(digit_sum, 0), num)
        
        return max_sum
