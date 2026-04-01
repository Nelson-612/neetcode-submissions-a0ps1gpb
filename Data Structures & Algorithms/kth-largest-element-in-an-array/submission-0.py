class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        nums.sort()
        return nums[-k]