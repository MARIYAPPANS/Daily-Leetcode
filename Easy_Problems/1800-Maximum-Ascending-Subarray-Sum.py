class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        m, c = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                c += nums[i]
            else:
                m = max(m, c)
                c = nums[i]
        return max(m, c)
