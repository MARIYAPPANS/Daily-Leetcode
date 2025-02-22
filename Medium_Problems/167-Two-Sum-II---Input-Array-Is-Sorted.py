class Solution:
    def twoSum(self, nums: List[int], tgt: int) -> List[int]:
        m = {}
        for i, n in enumerate(nums):
            c = tgt - n
            if c in m:
                return [m[c] + 1, i + 1]
            m[n] = i
        return []
