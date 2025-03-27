from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        c, m = 0, None
        for num in nums:
            if c == 0:
                m = num
            c += 1 if num == m else -1
        t = nums.count(m)
        l = 0
        for i in range(len(nums)):
            if nums[i] == m:
                l += 1
            r = t - l
            if l > (i + 1) // 2 and r > (len(nums) - i - 1) // 2:
                return i
        return -1
