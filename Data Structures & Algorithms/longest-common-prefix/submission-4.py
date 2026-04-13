class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = ""
        for i in range(len(strs[0])):
            for word in strs:
                if i >= len(word) or word[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result