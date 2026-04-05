class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows = len(board)
        cols = len(board[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs():
            queue = deque()

            for r in range(rows):
                for c in range(cols):
                    if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == "O":
                        queue.append((r, c))
                        board[r][c] = "T"

            while queue:
                r, c = queue.popleft()

                for dr, dc in direction:
                    newR, newC = r + dr, c + dc
                    if newR < 0 or newR >= rows or newC < 0 or newC >= cols:
                        continue
                    if board[newR][newC] == "O":
                        board[newR][newC] = "T"
                        queue.append((newR, newC))

        bfs()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X" 
                elif board[r][c] == "T":
                    board[r][c] = "O"