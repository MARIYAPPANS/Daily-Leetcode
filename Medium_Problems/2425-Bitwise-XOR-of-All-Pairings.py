class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums2) % 2 != 0:
            for num in nums1:
                ans ^= num
        if len(nums1) % 2 != 0:
            for num in nums2:
                ans ^= num
        return ans
