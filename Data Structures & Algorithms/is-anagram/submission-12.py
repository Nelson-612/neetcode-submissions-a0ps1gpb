class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}

        for w in s:
          if w not in seen_s:
            seen_s[w] = 1
          else:
            seen_s[w] += 1
          

        for w in t:
          if w not in seen_t:
            seen_t[w] = 1
          else:
            seen_t[w] += 1

        return seen_s == seen_t