class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0

        while maxHeap:
            cycle = n + 1
            temp = []

            while cycle > 0 and maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt != 0:
                    temp.append(cnt)
                cycle -= 1
                time += 1
            
            for cnt in temp:
                heapq.heappush(maxHeap, cnt)

            if maxHeap:
                time += cycle
            
        return time