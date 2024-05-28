class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if ch not in d:
                stack.append(ch)
            else:
                if len(stack) > 0 and stack[-1] == d[ch]:
                    stack.pop()
                else:
                    return False
        return not stack
