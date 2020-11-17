import tweepy
import csv

access_key = '#################'
access_secret = '#################'
consumer_key = '#################'
consumer_secret = '#################'

TOKEN="#################"
def search_tweets(text_query, number_of_tweets):
    # initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweets
    all_tweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.search(q=text_query, count=300, tweet_mode="extended")
    # print(new_tweets)
    all_tweets.extend(new_tweets)
    while len(new_tweets) > 0:
        if len(all_tweets) >= number_of_tweets - 100:
            break
        new_tweets = api.search(q=text_query, count=200, tweet_mode="extended")
        all_tweets.extend(new_tweets)
        print("...%s tweets extracted so far" % (len(all_tweets)))

    out_tweets = [[tweet.full_text.strip()] for tweet in all_tweets]

    # write the csv file
    with open('%s.csv' % text_query, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(out_tweets)
    pass


if __name__ == '__main__':
    # X is approximate number of tweets to be retrieved.
    search_tweets('from:realDonaldTrump', 300)
