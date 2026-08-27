from collections import defaultdict

class Twitter:

    def __init__(self):
        self.count = 0
        self.follows = defaultdict(set)
        self.tweet = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.tweet[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:

        res = []
        minHeap = []

        self.follows[userId].add(userId)
        for Id in self.follows[userId]:
            if Id in self.tweet:
                indx = len(self.tweet[Id]) - 1
                count, tweetId = self.tweet[Id][indx]
                heapq.heappush(minHeap, [count, tweetId, Id, indx - 1])
        
        while minHeap and len(res) < 10:
            count, tweetId, Id, indx = heapq.heappop(minHeap)
            res.append(tweetId)

            if indx >= 0:
                count, tweetId = self.tweet[Id][indx]
                heapq.heappush(minHeap, [count, tweetId, Id, indx - 1])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
