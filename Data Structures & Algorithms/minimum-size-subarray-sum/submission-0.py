class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        left = 0
        total = 0
        
        for right in range(len(nums)):
            total += nums[right]
            
            
            while total >= target:
                minLen = min(minLen, (right - left + 1))
                total -= nums[left]
                left += 1 
        if minLen != float('inf'):
            return minLen
        else:
            return 0