import twint
from .CsvReader import CsvReader
from .CsvWriter import CsvWriter
import Constant as C


def tweet_data():

    list_of_party = ["DemocratsList", "republicanList"]
    for listName in list_of_party:
        reader = CsvReader("TwitterUserList/" + listName)
        user_list = reader.getLines()
        for user in user_list:
            twitter_user_name = user.strip()[1:]
            c = twint.Config()
            c.Search = "from:" + twitter_user_name
            c.Store_object = True
            c.Limit = 100
            twint.run.Search(c)
            t_list = c.search_tweet_list
            tweet_list = []
            for tweetDetail in t_list:
                tweet_list.append(tweetDetail["tweet"].strip())
            file_name = "tweets/" + listName + "/" + twitter_user_name
            csv_writer = CsvWriter(file_name)
            csv_writer.write_to_file("\n".join(tweet_list))
            print("finished:" + twitter_user_name)


tweet_data()
