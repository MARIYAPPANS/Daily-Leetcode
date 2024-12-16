class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

     

        

        for i in range(k):
            minn=min(nums)
            c=nums.index(minn)
            nums[c]=minn*multiplier
        return nums

