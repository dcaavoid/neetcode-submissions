# For following relationship: use hash map (followerID: set(followeeID)) for O(1) follow and unfollow;
# For tweet posts: use hash map (userID: list(tweetID)) to get the lastest tweet through index.
# For get n tweets: Use max heap to append the last tweets each user posted;
#   Need an additional variable time to keep track the unique id for posting order;
#   Since max heap, time starts at 0 and decrement by 1 each time.

class Twitter:

    def __init__(self):
        self.time = 0          # Starts the first post at 0, then decrement by 1 for sorting tweets in a max heap.
        self.followMap = {}    # followerID: set(followeeId)
        self.tweetPosts = {}   # userID: list([time, tweetId])
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Create a new array of tweets for any users who haven't post any tweets yet.
        if userId not in self.tweetPosts:
            self.tweetPosts[userId] = []
        
        self.tweetPosts[userId].append([self.time, tweetId])
        self.time -= 1   # Unique time to track each tweet.


    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []   # max heap: [time, tweetId, followeeId, index]
        # A userId should follow itself for getting its own tweets.
        if userId not in self.followMap:
            self.followMap[userId] = set()
        
        self.followMap[userId].add(userId)

        # Use a max heap (min heap by sorting the -time) to sort the most recent tweets posted by all followees.
        # Store [time, tweetId, followeeId, index - 1] to track the next most recent tweets posted by followeeId.
        for followeeId in self.followMap[userId]:
            # If this user posts any tweets:
            if followeeId in self.tweetPosts:
                # Get most recent posts by this user.
                index = len(self.tweetPosts[followeeId]) - 1
                time, tweetId = self.tweetPosts[followeeId][index]
                maxHeap.append([time, tweetId, followeeId, index - 1])
        
        heapq.heapify(maxHeap)

        # Iterate the max heap until:
        # 1. there is no more tweets from the followees;
        # 2. or we have retrieved 10 most recent tweets.
        while maxHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            
            # Add next most recent tweets sent by followeeId if there is any tweets left.
            if index >= 0:
                time, tweetId = self.tweetPosts[followeeId][index]
                heapq.heappush(maxHeap, [time, tweetId, followeeId, index - 1])
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # Create a new set for any users who haven't follow anyone yet.
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Only unfollow if the follower is currently following the followeeID.
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)