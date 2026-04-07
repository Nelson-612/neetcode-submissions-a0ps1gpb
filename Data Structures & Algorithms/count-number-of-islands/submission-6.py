class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        count = 0

        def bfs(r,c):
            queue= deque()
            queue.append((r,c))
            visited.add((r,c))

            while queue:
                r, c = queue.popleft()
                direction = [(1,0), (-1,0), (0,1), (0,-1)]
                for dr, dc in direction:
                    newR = r + dr
                    newC = c + dc
                    if (newR < 0 or newR >= rows or newC < 0 or newC >= cols or (newR, newC) in visited or grid[newR][newC]=='0'):
                        continue
                    queue.append((newR, newC))
                    visited.add((newR, newC))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    count += 1
                    bfs(r,c)
        return count