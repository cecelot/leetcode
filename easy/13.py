BASE = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
MODIFIERS = {"V": 4, "X": 9, "L": 40, "C": 90, "D": 400, "M": 900}
PAIRINGS = [("I", "V"), ("I", "X"), ("X", "L"), ("X", "C"), ("C", "D"), ("C", "M")]


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        cursor = 0
        while cursor < len(s):
            cur = s[cursor]
            val = BASE[cur]
            if cursor + 1 < len(s):
                nxt = s[cursor + 1]
                if (cur, nxt) in PAIRINGS:
                    total += MODIFIERS[nxt]
                    cursor += 2
                    continue
            total += val
            cursor += 1
        return total
