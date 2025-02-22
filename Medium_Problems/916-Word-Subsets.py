from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        from collections import Counter
        
        max_count = Counter()
        for word in words2:
            max_count |= Counter(word)
        
        res = []
        for word in words1:
            if not (max_count - Counter(word)):
                res.append(word)
        
        return res
