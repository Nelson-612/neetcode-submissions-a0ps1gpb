class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count1 = {}
        for char in s1:
            count1[char] = count1.get(char, 0) + 1

        window= {}
        for i in range(len(s2)):
            window[s2[i]] = window.get(s2[i], 0) + 1

            if i >= len(s1):
                left = s2[i- len(s1)]
                window[left] -= 1
                if window[left] == 0:
                    del window[left]

            if window == count1:
                return True
        return False