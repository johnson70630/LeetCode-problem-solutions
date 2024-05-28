class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(ch for ch in s if ch.isalnum()).lower()
        left, right = 0, len(new_s)-1
        while right > left:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1
        return True
