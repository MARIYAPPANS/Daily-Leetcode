class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = set()
        n = len(s)
        
        for i in range(26):  # Iterate over each character from 'a' to 'z'
            char = chr(i + ord('a'))
            first = s.find(char)
            last = s.rfind(char)
            
            if first != -1 and last != -1 and first < last:
                for mid in set(s[first + 1:last]):
                    result.add((char, mid, char))
        
        return len(result)
