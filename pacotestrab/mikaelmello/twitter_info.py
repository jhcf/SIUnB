import argparse
import os
import tweepy
import sys
import re
import matplotlib.pyplot as plt
from tweepy.models import User
from wordcloud import WordCloud


class TwitterWrapper:
    def __init__(self, key, secret) -> None:
        auth = tweepy.AppAuthHandler(key, secret)
        self.api = tweepy.API(auth)

    def get_user(self, username) -> User:
        return self.api.get_user(username)

    def get_user_tweets(self, username, count=20):
        return list(self.api.user_timeline(username, count=count))

    def search(self, q, count=20, since_id=None, max_id=None):
        return self.api.search(
            q, count=count, since_id=since_id, max_id=max_id, result_type="recent"
        )

    def get_tweet_replies(self, tweet_id, count=20):
        tweet = self.api.get_status(tweet_id)
        author_name = tweet.author.screen_name

        query = f"to:{author_name}"

        replies = []
        since_id = int(tweet_id)
        max_id = None
        while True:
            results = self.search(query, since_id=since_id, max_id=max_id)

            dirty = False
            for result in results:
                if not max_id or max_id >= result.id:
                    max_id = result.id - 1

                if result.in_reply_to_status_id_str == tweet_id:
                    result.text = re.sub(f"(^@{author_name} )", "", result.text)
                    replies.append(result)
                    dirty = True
                if len(replies) >= count:
                    break

            if not dirty or len(replies) >= count:
                break

        return replies
