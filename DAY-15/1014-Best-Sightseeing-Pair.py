class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score, max_i = 0, values[0]  # max_i stores values[i] + i
        for j in range(1, len(values)):
            max_score = max(max_score, max_i + values[j] - j)
            max_i = max(max_i, values[j] + j)
        return max_score
