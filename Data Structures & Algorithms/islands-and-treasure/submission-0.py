class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        def addgrid(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or (r, c) in visit or grid[r][c] == -1):
                return 
            visit.add((r, c))
            q.append([r, c])
        # 先掃描整張地圖，把所有寶藏 0 都當成 BFS 起點
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        # dist 代表目前 BFS 是第幾層，距離最近寶藏幾步
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                # 目前這個位置距離最近寶藏的距離
                grid[r][c] = dist
                addgrid(r + 1, c)
                addgrid(r - 1, c)
                addgrid(r, c + 1)
                addgrid(r, c - 1)

            dist += 1

