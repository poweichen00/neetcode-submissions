class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        # 記錄已被佔用的正對角線
        posdia = set()
        # 記錄已被佔用的負對角線
        negdia = set()
        res = []
        # n×n 棋盤，全部填充 '.'
        board = [["."] * n for i in range(n)]
        def back(r):
            # 所有行都已成功放置皇后
            if r == n:
                # 當前棋盤轉換為字串列表
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            # 嘗試在當前行的每一列放置皇后
            for c in range(n):
                if c in col or (r + c) in posdia or (r - c) in negdia:
                    continue
                col.add(c)
                posdia.add(r+c)
                negdia.add(r-c)
                board[r][c] = "Q"
                back(r+1)
                col.remove(c)
                posdia.remove(r+c)
                negdia.remove(r-c)
                board[r][c] = "."
        # 從第 0 行開始回溯
        back(0)
        return res