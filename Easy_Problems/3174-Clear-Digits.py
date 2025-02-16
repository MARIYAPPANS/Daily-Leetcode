class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char.isdigit():
                if stack:  # Remove the closest non-digit character to the left
                    stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)
