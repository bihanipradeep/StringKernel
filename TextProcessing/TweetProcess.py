import twint
c = twint.Config()
c.Search = "yey"
c.Store_object = True
c.Limit = 100
twint.run.Search(c)
tlist = c.search_tweet_list
print("hacked that out")