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


def word_cloud(tweets):
    # Read the whole text.
    text = ""
    for t in tweets:
        cloud_text = re.sub(f"(https?:\/\/t\.co\/[A-Za-z\d]+)", "", t.text).lower()
        text += cloud_text
        text += "\n"

    # lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        add_help=True, description=("Retrieve Twitter info")
    )
    parser.add_argument(
        "action",
        type=str,
        choices=["user", "tweet"],
        help="Input dir for videos",
    )
    parser.add_argument(
        "url",
        type=str,
        help="URL of the user or tweet",
    )
    parser.add_argument("--wordcloud", action="store_true")

    args = parser.parse_args(sys.argv[1:])

    if not hasattr(args, "action"):
        print("Unrecognized command")
        parser.print_help()
        exit(1)

    if not os.environ["TWITTER_KEY"]:
        print("Application key missing")
        exit(1)

    if not os.environ["TWITTER_KEY_SECRET"]:
        print("Application key secret missing")
        exit(1)

    twitter = TwitterWrapper(
        os.environ["TWITTER_KEY"],
        os.environ["TWITTER_KEY_SECRET"],
    )

    if args.action == "user":
        matches = re.match("^https?:\/\/twitter\.com\/(\w+)(\/.*)?", args.url)
        username = matches.group(1)

        tweets = twitter.get_user_tweets(username)

        for t in tweets:
            print(f"@{t.author.screen_name}")
            print(t.text)
            print(t.created_at.strftime("%d/%m/%Y, %H:%M:%S"))
            print()

        if args.wordcloud:
            word_cloud(tweets)

    else:
        matches = re.match(
            "^https?:\/\/twitter\.com\/(\w+)\/status\/(\d+)(\/.*)?", args.url
        )
        tweet_id = matches.group(2)

        replies = twitter.get_tweet_replies(tweet_id, 10)
        for t in replies:
            print(f"@{t.author.screen_name}")
            print(t.text)
            print(t.created_at.strftime("%d/%m/%Y, %H:%M:%S"))
            print()

        if args.wordcloud:
            word_cloud(replies)
