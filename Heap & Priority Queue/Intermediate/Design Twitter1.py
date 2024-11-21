"""
Difficulty : Medium
Date created : 21-11-2024
"""

import heapq


class Twitter:
    # att timing element

    def __init__(self):
        self.users = {}
        self.time = 0
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.users:
            self.users[userId] = []
            self.follows[userId] = set()


        self.users[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> list[int]:

        posts = []
        heapq.heapify(posts)

        self.follows[userId].add(userId)

        for person in self.follows[userId]:
            for post in self.users[person]:
                heapq.heappush(posts, post)

        feed = []

        while posts and len(feed) < 10:
            feed.append(heapq.heappop(posts)[1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.follows:
            self.follows[followerId] = set()

        self.follows[followerId].add(followeeId)
        return None

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.follows:
            return None

        self.follows[followerId].discard(followeeId)

        return None


def main():

    twitter = Twitter()
    twitter.postTweet(1, 10)  # User 1 posts a new tweet with id = 10.
    twitter.postTweet(2, 20)  # User 2 posts a new tweet with id = 20.
    print(
        twitter.getNewsFeed(1)
    )  # User 1's news feed should only contain their own tweets -> [10].
    print(
        twitter.getNewsFeed(2)
    )  # User 2's news feed should only contain their own tweets -> [20].
    twitter.follow(1, 2)  # User 1 follows user 2.
    print(
        twitter.getNewsFeed(1)
    )  # User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
    print(
        twitter.getNewsFeed(2)
    )  # User 2's news feed should still only contain their own tweets -> [20].
    twitter.unfollow(1, 2)  # User 1 follows user 2.
    print(
        twitter.getNewsFeed(1)
    )  # User 1's news feed should only contain their own tweets -> [10].

    return None


if __name__ == "__main__":
    main()
