class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        tMap = Counter(t)
        window = {}
        have = 0
        need = len(tMap)
        result = ""
        resLen = float("inf")
        l = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in tMap and window[c] == tMap[c]:
                have += 1
            
            while have == need:
                if (right - l + 1) < resLen:
                    resLen = right - l + 1
                    result = s[l:right + 1]
                window[s[l]] -= 1
                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1

        return result