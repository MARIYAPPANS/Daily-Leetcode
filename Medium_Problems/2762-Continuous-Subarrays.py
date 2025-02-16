from collections import deque

class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_deque, max_deque = deque(), deque()
        count = 0
        left = 0
        
        for right in range(len(nums)):
            # Maintain min_deque (in increasing order)
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Maintain max_deque (in decreasing order)
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Shrink the window if the difference exceeds 2
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                left += 1
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()
            
            # Count the number of valid subarrays ending at 'right'
            count += (right - left + 1)
        
        return count
