#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD

import sys
import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import api as tweepy_api
from tweepy import Stream 
from tweepy import OAuthHandler 
from tweepy.models import Status
import app 
from app import db 
from models import Neighborhood, Source, Content
from shapely.geometry import box, Point 
from decimal import *
import traceback

#Ratings_24, Ratings_7day, Ratings_month, Ratings_year 
neighborhoods = Neighborhood()

consumer_key = '8vT4akwvPR1sWQIbO6y8g'
consumer_secret = '2YQxdvSVPerI51CoewMeIhyKsm8niwKZyuPIQAVg6s'
access_key= '21369282-5h31qLNIH68WoJIvfoU01DK191ixS8W9g67y41QQ'
access_secret= 'H2B6Ks97UbPs8XGxRFXNoXQpwO3Os4NTBvNi6b9B0w'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)
#query - opening connecting 

def bs(obj): #to_byte_string
    if isinstance(obj, str):
        return obj
    elif isinstance(obj, unicode):
        return obj.encode('utf-8')
    else:
        return obj

def build_boxes():
    box_to_nb = []
    for neighborhood in db.session.query(Neighborhood).all():
        box_to_nb.append([
            box(neighborhood.west_long, neighborhood.south_lat, neighborhood.east_long, neighborhood.north_lat), 
            neighborhood
        ])    
    return box_to_nb

def find_in_boxes(boxes, point):
    for box, neighborhood in boxes:
        if box.contains(point):
            print "This is neighborhood", neighborhood.name 
            return neighborhood

def tweets_from_search(handler):
    for tweet in tweepy.Cursor(api.search, q='san francisco').items(1000):
        handler(tweet)

class StreamListenerToHandler(StreamListener):
    def __init__(self, handler):
        self.handler = handler

    def on_data(self, data):
        tweet = Status.parse(tweepy_api, json.loads(data))
        self.handler(tweet)

    def on_error(self, status):
        print "something broken %s" % status

def tweets_from_stream(handler):
    stream = Stream(auth, StreamListenerToHandler(handler))
    stream.filter(track=['san francisco'])

def handle_tweet(tweet):
    global num_tweets
    num_tweets += 1
    print 'got tweet: %s' % bs(tweet.text)
    if num_tweets % 100 == 0:
        print "X" * 10, num_tweets
        # break
    content = Content()
    tweet_text = tweet.text
    tweetwhen = bs(tweet.created_at)
    s = tweet_text.split()
    #tags = set()
    for word in s:
        if word.startswith("#"):
            word = bs(word)
            if content.hashtags == None:
                content.hashtags = ""
            else:
                content.hashtags = content.hashtags + " " +word 
    content.message = tweet_text
    content.timestamp = tweetwhen

    if tweet.coordinates:
        print "tweet had a location"
        lat = tweet.coordinates["coordinates"][0]
        lon = tweet.coordinates["coordinates"][1]
        point = Point(lat, lon)

        neighborhood = find_in_boxes(boxes, point)
        if neighborhood is None:
            print "tweet didn't have a neighborhood"
            return
        print type(tweet_text)
        print bs(tweet_text)
        print neighborhood.name
        content.neighborhood_id = neighborhood.id
#        content.hashtags = " ".join(tags) 
    try:
        db.session.add(content)
        print ">>>>>> adding"
        db.session.commit()
    except Exception, e:
        print "error, not committing"
        traceback.print_exc()

if __name__ == '__main__':
    boxes = build_boxes()
    num_tweets = 0

    if False:
        tweets_from_search(handle_tweet)
    else:
        tweets_from_stream(handle_tweet)