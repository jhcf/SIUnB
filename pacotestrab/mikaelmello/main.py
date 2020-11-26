import argparse
import os
import tweepy
import sys
import re
import matplotlib.pyplot as plt
from tweepy.models import User
from wordcloud import WordCloud
from twitter_info import TwitterWrapper


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