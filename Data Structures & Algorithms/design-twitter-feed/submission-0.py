class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetmap = defaultdict(list) # userid -> [count, tweetid]
        self.followmap = defaultdict(set) # userid -> followid
    def postTweet(self, userId: int, tweetId: int) -> None:
        # 把這篇 tweet 存進該使用者的 tweet list
        self.tweetmap[userId].append([self.count, tweetId])
        # 越新的 tweet count 越小，例如：舊 : -1, 新: -5
        # -5 會比 -1 更早被 pop 出來
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = [] # [count, tweetId, followeeId, next tweet 的 index]
        # 使用者自己的 tweet 也要出現在自己的動態牆，把自己加入 followMap
        self.followmap[userId].add(userId)

        # 看 userId 追蹤的所有人
        for followeeId in self.followmap[userId]:
            # 這個人至少有發過 tweet
            if followeeId in self.tweetmap:
                # 取這個人的「最後一篇 tweet」，最後一個就是最新的
                index = len(self.tweetmap[followeeId]) - 1
                # 拿出最新 tweet 的時間和 tweetId
                count, tweetId = self.tweetmap[followeeId][index]

                heapq.heappush(minheap, [count, tweetId, followeeId, index-1])
        while minheap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minheap)
            res.append(tweetId)

            # 如果這個 followee 還有更舊的 tweet
            if index >= 0:
                # 取得這個人的下一篇 tweet
                count, tweetId = self.tweetmap[followeeId][index]
                # 再放回 heap 下一輪會繼續跟其他人的 tweet 比誰更新
                heapq.heappush(minheap, [count, tweetId, followeeId, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)

