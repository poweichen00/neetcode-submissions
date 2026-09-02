class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))
        minute = 0
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in direct:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r, c) not in visit):
                        grid[r][c] == 2
                        fresh -= 1
                        q.append((r, c))
                        visit.add((r, c))
            minute += 1
        return minute if fresh == 0 else -1
