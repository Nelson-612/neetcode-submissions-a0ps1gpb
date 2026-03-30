class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def bfs(queue, visited):
            direction = [(1,0),(-1,0),(0,1),(0,-1)]
            while queue:
                r, c = queue.popleft()
                for dr, dc in direction:
                    newR = r + dr
                    newC = c + dc
                    if newR < 0 or newR >= rows:
                        continue
                    if newC < 0 or newC >= cols:
                        continue
                    if (newR, newC) in visited:
                        continue
                    if heights[newR][newC] >= heights[r][c]:
                        visited.add((newR, newC))
                        queue.append((newR, newC))

        pac_queue = deque()
        pac_visited = set()
        for c in range(cols):
            pac_queue.append((0,c))
            pac_visited.add((0,c))
        for r in range(rows):
            pac_queue.append((r,0))
            pac_visited.add((r,0))

        atl_queue = deque()
        atl_visited = set()
        for c in range(cols):
            atl_queue.append((rows -1,c))
            atl_visited.add((rows -1,c))
        for r in range(rows):
            atl_queue.append((r,cols-1))
            atl_visited.add((r,cols -1))

        
        bfs(pac_queue, pac_visited)
        bfs(atl_queue, atl_visited)

        return [[r,c] for r, c in pac_visited & atl_visited]
                    
    