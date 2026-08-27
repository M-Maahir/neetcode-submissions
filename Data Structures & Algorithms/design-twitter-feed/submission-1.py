class Twitter:

    def __init__(self):

        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []

        self.followMap[userId].add(userId)
        for followId in self.followMap[userId]:
            if followId in self.tweetMap:
                idx = len(self.tweetMap[followId]) - 1
                count, tweetId = self.tweetMap[followId][idx]
                heapq.heappush(heap,[count, tweetId, followId, idx - 1])

        while heap and len(res) < 10:

            count, tweetId, followId, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx >= 0:
                count, tweetId = self.tweetMap[followId][idx]
                heapq.heappush(heap, [count, tweetId, followId, idx - 1])
        
        
        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
