class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Calculate sum of each window of size k
        window_sums = [sum(nums[:k])]
        for i in range(1, n - k + 1):
            window_sums.append(window_sums[-1] - nums[i - 1] + nums[i + k - 1])
        
        # Left and right indices
        left = [0] * len(window_sums)
        right = [0] * len(window_sums)
        
        max_index = 0
        for i in range(len(window_sums)):
            if window_sums[i] > window_sums[max_index]:
                max_index = i
            left[i] = max_index
        
        max_index = len(window_sums) - 1
        for i in range(len(window_sums) - 1, -1, -1):
            if window_sums[i] >= window_sums[max_index]:
                max_index = i
            right[i] = max_index
        
        # Find the best combination of three subarrays
        max_sum = 0
        result = []
        for i in range(k, len(window_sums) - k):
            total = window_sums[left[i - k]] + window_sums[i] + window_sums[right[i + k]]
            if total > max_sum:
                max_sum = total
                result = [left[i - k], i, right[i + k]]
        
        return result
