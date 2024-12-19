class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_val = res = 0
        for i, val in enumerate(arr):
            max_val = max(max_val, val)
            if max_val == i:
                res += 1
        return res
