class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows= len(grid)
        cols=len(grid[0])
        queue = deque()
        INF = 2**31 - 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j))

        directions = [(1,0), (-1,0),(0,1), (0,-1)] 
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                newR = r + dr
                newC = c + dc
                if newR <0 or newR >= rows:
                    continue
                if newC < 0 or newC >= cols:
                    continue
                if grid[newR][newC] != INF:
                    continue
                grid[newR][newC] = grid[r][c] + 1
                queue.append((newR, newC))
