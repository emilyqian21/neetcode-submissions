class Solution:
    def solve(self, board: List[List[str]]) -> None:
        from collections import deque
        nrow = len(board)
        ncol = len(board[0])
        q = deque()

        # 将边界上的 O 加入 queue
        for r in range(nrow):
            if board[r][0] == "O":
                board[r][0] = "T"
                q.append((r, 0))

            if board[r][ncol - 1] == "O":
                board[r][ncol - 1] = "T"
                q.append((r, ncol - 1))

        for c in range(ncol):
            if board[0][c] == "O":
                board[0][c] = "T"
                q.append((0, c))

            if board[nrow - 1][c] == "O":
                board[nrow - 1][c] = "T"
                q.append((nrow - 1, c))

        # 从所有边界 O 同时开始 BFS
        while q:
            r, c = q.popleft()

            for nr, nc in [
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1)
            ]:
                if (
                    0 <= nr < nrow
                    and 0 <= nc < ncol
                    and board[nr][nc] == "O"
                ):
                    # 加入 queue 时立刻标记，避免重复加入
                    board[nr][nc] = "T"
                    q.append((nr, nc))

        # 剩余 O 被包围；T 是安全的 O
        for r in range(nrow):
            for c in range(ncol):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"