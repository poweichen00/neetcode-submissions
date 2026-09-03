class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visit = set()
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows-1 or c == 0 or c == cols-1) and board[r][c] == 'O':
                    q.append((r, c))
                    visit.add((r, c))
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in direct:
                    r, c = row + dr, col + dc 
                    if (r in range(rows) and
                        c in range(cols) and
                        board[r][c] == 'O' and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visit:
                    board[r][c] = 'X'

