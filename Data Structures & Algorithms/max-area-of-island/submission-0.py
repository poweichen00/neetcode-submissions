class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxcount = 0
        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            count = 0
            while q:
                row, col = q.popleft()
                count += 1
                direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in direct:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r, c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxcount = max(maxcount, bfs(r, c))
        return maxcount