class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True

        dp = [False] *(len(s) + 1)
        dp[0] = True
        wordSet = set(wordDict)

        for i in range(len(s)):
            if dp[i]:
                for word in wordSet:
                    if s[i:i+len(word)] == word:
                        dp[i + len(word)] = True

        return dp[len(s)]