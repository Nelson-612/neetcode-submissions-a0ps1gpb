class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Map = {}
        for c in s1:
            s1Map[c] = s1Map.get(c, 0) + 1

        windowMap = {}
        for i in range(len(s2)):
            windowMap[s2[i]] = windowMap.get(s2[i], 0) + 1

            if i >= len(s1):
                left = s2[i - len(s1)]
                windowMap[left] -= 1
                if windowMap[left] == 0:
                    del windowMap[left]

            if windowMap == s1Map:
                return True
        return False