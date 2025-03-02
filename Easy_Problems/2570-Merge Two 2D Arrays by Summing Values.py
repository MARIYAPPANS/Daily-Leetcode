from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = {}
        for i, v in nums1 + nums2:
            d[i] = d.get(i, 0) + v
        return sorted([[k, v] for k, v in d.items()])
