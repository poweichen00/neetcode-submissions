class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endofword = True

    def search(self, word: str) -> bool:
        # j: 目前要處理的 word 的字元索引
        # root: 目前在 Trie 樹中所在的節點
        def dfs(j, root):
            cur = root
            # 從索引 j 開始，逐一檢查 word 中的每個字元
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    # '.' 可以匹配任何字元，必須嘗試當前節點下的所有子節點
                    for child in cur.children.values():
                        # dfs，檢查下一個字元 i + 1 是否能從這個 child 節點成功匹配
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endofword
        # 從 word 的第 0 個字元開始，從 Trie 的根節點 DFS 搜尋
        return dfs(0, self.root)





