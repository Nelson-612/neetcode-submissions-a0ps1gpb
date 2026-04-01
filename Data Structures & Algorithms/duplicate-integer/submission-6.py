class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False