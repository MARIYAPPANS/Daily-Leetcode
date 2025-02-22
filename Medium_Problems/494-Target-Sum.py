class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for num in nums:
            temp = {}
            for s in dp:
                temp[s + num] = temp.get(s + num, 0) + dp[s]
                temp[s - num] = temp.get(s - num, 0) + dp[s]
            dp = temp
        return dp.get(target, 0)
