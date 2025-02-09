from typing import List
from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2  # Total number of pairs
        count = defaultdict(int)
        good_pairs = 0

        for i, num in enumerate(nums):
            diff = num - i
            good_pairs += count[diff]  # Count previously seen good pairs
            count[diff] += 1

        return total_pairs - good_pairs  # Bad pairs = total pairs - good pairs
