"""
Difficulty : Medium
Date created : 04-12-2024
"""

import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.posts = defaultdict(list)  # [time, post]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        tweets = []
        heapq.heapify(tweets)

        self.users[userId].add(userId)
        for user in self.users[userId]:
            for post in self.posts[user]:
                heapq.heappush(tweets, post)

        res = []
        while tweets and len(res) < 10:
            res.append(heapq.heappop(tweets)[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)


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

    [
        "Twitter",
        "postTweet",
        [7, 23],
        "postTweet",
        [7, 24],
        "postTweet",
        [7, 25],
        "postTweet",
        [7, 26],
        "follow",
        [8, 7],
        "getNewsFeed",
        [8],
        "follow",
        [8, 7],
        "unfollow",
        [8, 7],
        "getNewsFeed",
        [8],
        "postTweet",
        [7, 27],
        "unfollow",
        [8, 7],
        "getNewsFeed",
        [8],
    ]
    return None


if __name__ == "__main__":
    main()
