class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # 從樹的根節點開始
        cur = self.root
        # 把單字拆成一個個字元，("cat" 會依序取出 'c', 'a', 't')
        for c in word:
            # 目前節點的 children 字典中，有沒有這個字元 'c' 的分支
            if c not in cur.children:
                # 沒有，就建立一個新的節點，它放入 children 中
                cur.children[c] = TrieNode()
            # 無論是新建立的還是原本就存在的，都將 cur 往下移動到該字元的節點
            cur = cur.children[c]
        cur.endofword = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        # True：一個完整被插入過的單字 ("app"，且 "app" 曾被插入)
        # False：某個更長單字的前綴 (有 "apple"，但我們搜尋 "app")
        return cur.endofword

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        # 只要路徑走得通，有單字是以這個 prefix 開頭的
        return True
        