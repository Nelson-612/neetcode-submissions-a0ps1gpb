class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]