class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        visited = set()
        shape = set()
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            path = []
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                path.append((row - r, col - c))  # relative position

                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr, dc in directions:
                    newR = row + dr
                    newC = col + dc
                    if (newR < 0 or newR >= rows or
                        newC < 0 or newC >= cols or
                        (newR, newC) in visited or
                        grid[newR][newC] == 0):
                        continue
                    visited.add((newR, newC))
                    queue.append((newR, newC))

            return tuple(path)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    shape.add(bfs(r, c))

        return len(shape)