class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:]=nums2
        nums1.sort()


        '''Aother way
        nums1[:m + n] = sorted(nums1[:m] + nums2)
        '''
        


        