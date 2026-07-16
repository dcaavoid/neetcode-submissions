class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = {}      # userId: [(time, tweetId)]
        self.followMap = {}     # followerId: set(followeeId)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1     # For max heap
        
    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow(userId, userId)
        maxHeap =[]
        res = []

        # For each followee, get the most recent tweetId and append to max heap.
        for followeeId in self.followMap[userId]:
            if followeeId not in self.tweetMap:
                continue
            
            index = len(self.tweetMap[followeeId]) - 1
            t, tweetId = self.tweetMap[followeeId][index]
            heapq.heappush(maxHeap, (t, tweetId, followeeId, index - 1))
        
        # Add most recent tweet to the result, and update the next most recent tweet from that followee.
        # Stop if there are less than 10 tweets.
        while maxHeap and len(res) != 10:
            _, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                t, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, (t, tweetId, followeeId, index - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
