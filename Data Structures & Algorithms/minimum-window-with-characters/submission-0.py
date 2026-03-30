class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        tMap = {}
        for c in t:
            tMap[c] = tMap.get(c, 0) + 1

        cMap = {}
        left = 0
        have, need = 0, len(tMap)
        result = ""
        resLen = float("inf")
        for right in range(len(s)):
            c = s[right]
            cMap[c] = cMap.get(c, 0) + 1
            if c in tMap and cMap[c] == tMap[c]:
                have += 1
            while have == need:
                if right - left + 1 < resLen:
                    resLen = right -left + 1
                    result = s[left:right+1]
                cMap[s[left]] -= 1
                if s[left] in tMap and cMap[s[left]] < tMap[s[left]]:
                    have -= 1
                left += 1
        return result


        