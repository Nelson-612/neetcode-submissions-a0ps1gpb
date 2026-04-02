class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        heap = []
        users = self.follows[userId] | {userId}

        for user in users:
            if user in self.tweets:
                idx = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][idx]
                heapq.heappush(heap, (-time, tweetId, user, idx - 1))

        result = []
        while heap and len(result) < 10:
            time, tweetId, user, idx = heapq.heappop(heap)  
            result.append(tweetId)                           
            if idx >= 0:                                     
                time, tweetId = self.tweets[user][idx]
                heapq.heappush(heap, (-time, tweetId, user, idx - 1))
        return result

    def follow(self, followerId, followeeId):
        self.follows[followerId].add(followeeId)    

    def unfollow(self, followerId, followeeId):
        self.follows[followerId].discard(followeeId) 