class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = {0: -1}
        runningSum = 0

        for i,n in enumerate(nums):
            runningSum += n
            remainder = runningSum % k

            if remainder in prefixSum and i - prefixSum[remainder] >= 2:
                return True
            if remainder not in prefixSum:
                prefixSum[remainder] = i
        return False