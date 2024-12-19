class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps, curr_end, curr_furthest = 0, 0, 0
        for i in range(len(nums) - 1):
            curr_furthest = max(curr_furthest, i + nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = curr_furthest
        return jumps
