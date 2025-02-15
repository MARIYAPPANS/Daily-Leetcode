class Solution:
    def canPartition(self, num, target):
        if target < 0 or num < target:
            return False
        if num == target:
            return True
        
        p, d = 1, 10
        while p <= num:
            if self.canPartition(num // d, target - num % d):
                return True
            p, d = p * 10, d * 10
        return False

    def punishmentNumber(self, n):
        return sum(i * i for i in range(1, n + 1) if self.canPartition(i * i, i))
