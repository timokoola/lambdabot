# coding=utf-8
from __future__ import print_function
from twython import Twython
from twython.exceptions import TwythonError


class TwythonHelper:

    def __init__(self, keyfile):
        f = open(keyfile)
        lines = f.readlines()
        f.close()
        self.consumerkey = lines[0].strip()
        self.consumersecret = lines[1].strip()
        self.accesstoken = lines[2].strip()
        self.accesssec = lines[3].strip()

        self.api = Twython(self.consumerkey, self.consumersecret, self.accesstoken, self.accesssec)

helper = (TwythonHelper("keys.keys"))
api = helper.api
query = u"芬兰"

def handler(event, context):
    results = api.search(q=query,result_type="recent")
    for tweet in results["statuses"]:
        text = tweet["text"]
        if text.startswith("RT"):
        	print("%s is a RT, skipping" % text)
        	continue
        # re.search matches anywhere in the string; re.I means case-insensitive
        
        print(tweet["text"])
        # client.retweet will raise an error if we try to retweet a tweet
        # that we've already retweeted. to avoid having to keep track, we
        # just use a try/except block
        try:
            api.retweet(id=tweet["id"])
        except TwythonError as e:
            print(e)

