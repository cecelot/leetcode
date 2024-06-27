class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minLength = min([len(s) for s in strs])
        common = ""
        for i in range(0, minLength):
            testChar = strs[0][i]
            result = [*filter(lambda s: s[i] == testChar, strs)]
            if len(result) != len(strs):
                return common
            common += testChar
        return common
