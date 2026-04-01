class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:  # start of sequence
                length = 1
                while num + 1 in numSet:
                    num += 1
                    length += 1
                longest = max(longest, length)
        
        return longest