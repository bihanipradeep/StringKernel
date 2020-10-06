# coding: utf-8
# import twint
# # from . import CsvReader
# # from . import CsvWriter
# # import Constant as C
#
#
# def tweet_data():
#     list_of_party = ["DemocratsList", "republicanList"]
#     for listName in list_of_party:
#         reader = CsvReader("TwitterUserList/" + listName)
#         user_list = reader.getLines()
#         for user in user_list:
#             twitter_user_name = user.strip()[1:]
#             c = twint.Config()
#             c.Search = "from:" + twitter_user_name
#             c.Store_object = True
#             c.Limit = 100
#             twint.run.Search(c)
#             t_list = c.search_tweet_list
#             tweet_list = []
#             for tweetDetail in t_list:
#                 tweet_list.append(tweetDetail["tweet"].strip())
#             file_name = "tweets/" + listName + "/" + twitter_user_name
#             # csv_writer = CsvWriter(file_name)
#             # csv_writer.write_to_file("\n".join(tweet_list))
#             # print("finished:" + twitter_user_name)
#
#
# def get_user_tweet_data(user_name):
#     twitter_user_name = user_name.strip()[1:]
#     c = twint.Config()
#     c.Search = "from:" + twitter_user_name
#     c.Store_object = True
#     c.Limit = 100
#     twint.run.Search(c)
#     t_list = c.search_tweet_list
#     tweet_list = []
#     for tweetDetail in t_list:
#         tweet_list.append(tweetDetail["tweet"].strip())
#     return tweet_list
#
#
# print(get_user_tweet_data("RTErdogan"))

import tweepy  # https://www.tweepy.org
import csv

access_key = '1086883669-3JBHHKJSq4B3XvR7QzQSPp0F5vZgE8F8Q0Tbch7'
access_secret = 'O6lwPwyk7FGSgCM0SGoK4wqnBSc8FVsXphnBPV2gtAvo2'
consumer_key = 'X0KmIw30RBh9FdA0re0P1VZq4'
consumer_secret = 'BBcxT6QwtcAwth6hMkHROHX01CeKsmpsWIVBGIW3omOhjWKwnI'

TOKEN="AAAAAAAAAAAAAAAAAAAAAKIrIAEAAAAA9%2Bvz8xvU1TBb2j2f44hNnxGNAos%3DMKrAhsmgMm2xJLEWT0LUwSnEkrhUzp9FFcbgR4aOulVq5oFtTv"
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
    # while len(new_tweets) > 0:
    #     if len(all_tweets) >= number_of_tweets - 100:
    #         break
    #     new_tweets = api.search(q=text_query, count=200, tweet_mode="extended")
    #     all_tweets.extend(new_tweets)
    #     print("...%s tweets extracted so far" % (len(all_tweets)))

    out_tweets = [[tweet.full_text.strip()] for tweet in all_tweets]

    # write the csv file
    with open('%s.csv' % text_query, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(out_tweets)
    pass


if __name__ == '__main__':
    # X is approximate number of tweets to be retrieved.
    search_tweets('from:realDonaldTrump', 300)
