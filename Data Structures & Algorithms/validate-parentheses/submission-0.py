class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for char in s:
            if char in bracket_map:
                stack.append(char)
            elif char in bracket_map.values():
                if not stack:
                    return False
                
                opening = stack.pop()
                if bracket_map[opening] != char:
                    return False

        return len(stack) == 0