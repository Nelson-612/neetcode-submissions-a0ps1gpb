class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        heap = [(0,0,0)]
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()

        while heap:
            effort, row, col = heapq.heappop(heap)

            if (row, col) in visited:
                continue
            visited.add((row,col))
            if row == rows -1 and col == cols-1:
                return effort

            for dr, dc in direction:
                newR = row + dr
                newC = col + dc
                if 0 <= newR < rows and 0 <= newC < cols:
                    new_effort = max(effort, abs(heights[newR][newC] - heights[row][col]))
                    heapq.heappush(heap, (new_effort, newR, newC))

                