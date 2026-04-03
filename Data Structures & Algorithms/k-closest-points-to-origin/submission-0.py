class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []

        heap = []
        for x, y in points:
            distance = x*x + y*y
            heapq.heappush(heap, (distance, x,y))

        result = []
        for i in range(k):
            distance, x, y = heapq.heappop(heap)
            result.append([x,y])
        
        return result