class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)

        for str in strs:
            charList = [0] * 26

            for c in str:
                charList[ord(c) - ord('a')] += 1
            strMap[tuple(charList)].append(str)
        return list(strMap.values())