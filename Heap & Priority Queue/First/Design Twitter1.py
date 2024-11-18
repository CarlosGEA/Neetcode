"""
Difficulty : Medium
Date created : 18-11-2024
"""


class Twitter:

    def __init__(self):
        self.users = {}
        self.posts = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users.setdefault(userId, set())
        self.posts.append([userId, tweetId])
        return None

    def getNewsFeed(self, userId: int) -> list[int]:

        feed = []
        for user, tweet in self.posts[::-1]:

            if len(feed) >= 10:
                break

            if user in self.users[userId] or user == userId:
                feed.append(tweet)

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.users:
            self.users.setdefault(followerId, set())

        self.users[followerId].add(followeeId)
        return None

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # if followerId == followeeId or followeeId not in self.users[followerId]:
        #     return None

        self.users[followerId].discard(followeeId)
        return None


def main():

    twitter = Twitter()
    twitter.postTweet(1, 10)  # User 1 posts a new tweet with id = 10.
    twitter.postTweet(2, 20)  # User 2 posts a new tweet with id = 20.
    print(twitter.getNewsFeed(1))  # User 1's news feed only own tweets -> [10].
    print(twitter.getNewsFeed(2))  # User 2's news feed only own tweets -> [20].
    twitter.follow(1, 2)  # User 1 follows user 2.
    print(twitter.getNewsFeed(1))  # User 1's news feed from both user 1 and user 2 -> [20, 10].
    print(twitter.getNewsFeed(2))  # User 2's news feed still only  own tweets -> [20].
    twitter.unfollow(1, 2)  # User 1 follows user 2.
    print(twitter.getNewsFeed(1))  # User 1's news feed only own tweets -> [10].

    ["Twitter", "postTweet", [7, 23], "postTweet", [7, 24], "postTweet", [7, 25], "postTweet", [7, 26], 
     "follow", [8, 7], "getNewsFeed", [8], "follow", [8, 7], "unfollow", [8, 7], "getNewsFeed", [8], 
     "postTweet", [7, 27], "unfollow", [8, 7], "getNewsFeed", [8]]
    return None


if __name__ == "__main__":
    main()
