class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        lo = s[0 : len(s) // 2]
        hi = reversed(s[len(s) // 2 :])
        for a, b in zip(lo, hi):
            if a != b:
                return False
        return True
