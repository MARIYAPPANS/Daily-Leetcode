class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ways = 0
        left_sum = 0
        total_sum = sum(nums)
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            if left_sum >= total_sum - left_sum:
                ways += 1
        return ways
