class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (days[-1] + 1)
        day_set = set(days)

        for i in range(1, days[-1] + 1):
            if i not in day_set:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0],  # 1-day pass
                    dp[max(0, i - 7)] + costs[1],  # 7-day pass
                    dp[max(0, i - 30)] + costs[2]  # 30-day pass
                )
        
        return dp[days[-1]]
