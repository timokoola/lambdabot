# coding=utf-8
from __future__ import print_function
from twython import Twython
from twython.exceptions import TwythonError
import keys

# inspired by http://joelgrus.com/2015/12/30/polyglot-twitter-bot-part-3-python-27-aws-lambda/

class TwythonHelper:

    def __init__(self):
        self.consumerkey = keys.line1
        self.consumersecret = keys.line2
        self.accesstoken = keys.line3
        self.accesssec = keys.line4

        self.api = Twython(self.consumerkey, self.consumersecret, self.accesstoken, self.accesssec)

helper = TwythonHelper()
api = helper.api
query = u"芬兰"

def handler(event, context):
    results = api.search(q=query,result_type="recent")
    for tweet in results["statuses"]:
        text = tweet["text"]
        if text.startswith("RT"):
        	print("%s is a RT, skipping" % text)
        	continue
        
        print(tweet["text"])
        try:
            api.retweet(id=tweet["id"])
        except TwythonError as e:
            print(e)

