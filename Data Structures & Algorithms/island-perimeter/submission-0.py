class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        def bfs(r,c):
            queue= deque()
            queue.append((r,c))
            visited.add((r,c))
            perimeter = 0

            while queue:
                r,c = queue.popleft()
                for dr, dc in direction:
                    newR = r + dr
                    newC = c + dc
                    if (newR < 0 or newR >= rows or newC < 0 or newC >= cols or grid[newR][newC] == 0 ):
                        perimeter += 1
                    elif (newR, newC) not in visited:
                        visited.add((newR,newC))
                        queue.append((newR, newC))

            return perimeter

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return bfs(r, c)
        return 0
                    
        