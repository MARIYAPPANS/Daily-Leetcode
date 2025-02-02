class Solution:
    def check(self, nums: List[int]) -> bool:
        count_descends = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count_descends += 1
                if count_descends > 1:
                    return False
        
        return True
