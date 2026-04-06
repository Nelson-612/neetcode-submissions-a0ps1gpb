class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2**31 - 1
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))

        direction = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in direction:
                newR = r + dr
                newC = c + dc
                if (newR < 0 or newR >= rows or newC <0 or newC >= cols or grid[newR][newC] != INF):
                    continue
                grid[newR][newC] = grid[r][c] + 1
                queue.append((newR,newC))
