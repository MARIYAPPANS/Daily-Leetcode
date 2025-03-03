from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l, m, r = [], [], []
        for x in nums:
            if x < pivot:
                l.append(x)
            elif x > pivot:
                r.append(x)
            else:
                m.append(x)
        return l + m + r
