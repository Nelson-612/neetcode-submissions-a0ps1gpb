class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1


        if fresh == 0:
            return 0

        minutes = 0
        direction = [(1,0), (-1,0), (0,1), (0, -1)]
        while queue:
            for i in range(len(queue)):
                r , c = queue.popleft()
                for dr, dc in direction:
                    newR = dr + r
                    newC = dc + c
                    if (newR < 0 or newR >= rows or newC < 0 or newC >= cols or grid[newR][newC] != 1):
                        continue
                    grid[newR][newC] =2
                    fresh -= 1
                    queue.append((newR, newC))
            minutes += 1
        return minutes - 1 if fresh == 0 else -1

