MATCHES = {"(": ")", "{": "}", "[": "]"}


class Solution:
    def isValid(self, s: str) -> bool:
        opened = []
        for brace in s:
            if brace in MATCHES.values():
                if len(opened) == 0:
                    return False
                if MATCHES[opened[-1]] != brace:
                    return False
                opened.pop()
            else:
                opened.append(brace)
        return len(opened) == 0


print(Solution().isValid("()"))
