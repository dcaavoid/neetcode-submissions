# Use a hash map (userId: [list of userId's])
# Use minHeap (time, tweetId) -> one minHeap for each user?
# Build a temporary minHeap in getNewsFeed()

class Twitter:

    def __init__(self):
        self.following = {} # userId: set of followeeId
        self.time = 0   # -time for maxHeap starting from -1
        self.tweets = {} # userId: list of (-time, tweetId)
    
    def postTweet(self, userId: int, tweetId: int):
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.time -= 1
        self.tweets[userId].append((self.time, tweetId))
    
    def getNewsFeed(self, userId: int) -> List[int]:
        # Merge k sorted list
        self.follow(userId, userId)
        res = []    # tweetId from most recent to least recent
        maxHeap = []    # (-time, tweetId)

        # Get the most recent tweet from each followeeId
        for followeeId in self.following[userId]:
            # Skip if followeeId did not post
            if followeeId not in self.tweets:
                continue
            
            # Index for future visit of this tweets list
            index = len(self.tweets[followeeId]) - 1
            t, tweetId = self.tweets[followeeId][index]
            heapq.heappush(maxHeap, (t, tweetId, followeeId, index - 1))
        
        # Add most recent tweet from maxHeap to result
        # Update pointer to next most recent tweet from that followee
        while maxHeap and len(res) != 10:
            _, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)

            if index >= 0:
                t, tweetId = self.tweets[followeeId][index]
                heapq.heappush(maxHeap, (t, tweetId, followeeId, index - 1))
        
        return res

    
    def follow(self, followerId: int, followeeId: int):
        if followerId not in self.following:
            # User follow itself to get its own tweets
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int):
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
