class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        direction = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(r,c):
            queue = deque() 
            queue.append((r,c))
            visited.add((r,c))
            area = 1

            while queue:
                r, c = queue.popleft()
                for dr, dc in direction:
                    newR = r + dr
                    newC = c + dc
                    if (newR < 0 or newR >= rows or newC < 0 or newC >= cols or grid[newR][newC] == 0 or (newR,newC) in visited):
                        continue
                    visited.add((newR, newC))
                    queue.append((newR, newC))
                    area += 1
            return area
            
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    maxArea = max(maxArea, area)
        return maxArea
