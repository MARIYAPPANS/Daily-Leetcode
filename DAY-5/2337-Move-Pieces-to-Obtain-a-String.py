class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Filter out the underscores and check if L and R are in the same order
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        # Check the positions of 'L' in start and target
        j = 0
        for i, c in enumerate(start):
            if c == 'L':
                while target[j] != 'L':
                    j += 1
                if i < j:  # 'L' can only move left
                    return False
                j += 1
        
        # Check the positions of 'R' in start and target
        j = 0
        for i, c in enumerate(start):
            if c == 'R':
                while target[j] != 'R':
                    j += 1
                if i > j:  # 'R' can only move right
                    return False
                j += 1
        
        return True
