class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    def addword(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        # 所有要搜尋的單字插入 Trie 中
        # 在 DFS 時可以隨時檢查「目前拼湊的字串前綴」是否存在於字典中，若不存在即可提前剪枝，大幅減少無效搜尋。
        for w in words:
            root.addword(w)

        row, col = len(board), len(board[0])
        res, visit = set(), set()
        # node: 目前在 Trie 樹中的節點
        # word: 目前累積拼湊出的字串
        def dfs(r, c, node, word):
            # 核心剪枝 / 終止條件
            # 超出棋盤邊界、座標已經走過、棋盤上的字母不在當前 Trie 節點的子節點
            if (r < 0 or c < 0 or r >= row or c >= col or (r, c) in visit or board[r][c] not in node.children):
                return
            visit.add((r, c))
            # 沿著 Trie 往下走，並將當前字母加入累積字串
            node = node.children[board[r][c]]
            word += board[r][c]
            # 檢查當前 Trie 節點是否標記為完整單字
            # 如果是，代表我們成功在棋盤上找到了一個字典裡的單字，將其加入結果集合
            if node.word:
                res.add(word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visit.remove((r, c))
        for r in range(row):
            for c in range(col):
                dfs(r, c, root, "")
        return list(res)

