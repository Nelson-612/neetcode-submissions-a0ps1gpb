class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                current = num
                while current + 1 in numSet:
                    length += 1
                    current += 1
                longest = max(longest, length)
        return longest