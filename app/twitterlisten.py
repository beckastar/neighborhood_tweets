#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD
#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD

import sys
import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import Stream 
from tweepy import OAuthHandler 
import pygeocoder
from pygeocoder import Geocoder
#from models import Neighborhood, Source, Content, Ratings_24, Ratings_7day, Ratings_month, Ratings_year as db_session

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


for tweet in tweepy.Cursor(api.search, q='san francisco').items(100):
	#
	if tweet.coordinates :
		#import pdb;pdb.set_trace()
		print bs(tweet.text), bs(tweet.created_at), bs(tweet.coordinates)
		coordinates = tweet.coordinates['coordinates']
		#print coordinates
#		print gmaps.latlng_to_address(coordinates[0], coordinates[1])
		#store into database
		print bs("Geocoding: %r, %r" % (coordinates[0],coordinates[1]))
		results= Geocoder.reverse_geocode(coordinates[1],coordinates[0])
		print bs("Results: %s" % results)
		print "\n"


'''
class CustomStreamListener(tweepy.StreamListener):
#listener can be registered to twitter.api and it sends output whenever there is a message
    def __init__(self):
        super(CustomStreamListener, self).__init__()
        self.num_read = 0

    def on_status(self, status):
	if status.geo:
	    with open('tweet_data_json_19.txt', 'a') as outfile:
		output = {}
		output['screen_name'] = status.author.screen_name
		output['coordinates'] = status.coordinates
		output['text'] = status.text
		output['created_at'] = status.created_at.strftime('%Y-%m-%dT%H:%M:%S')
                outfile.write(json.dumps(output))

	if self.num_read > 14000:
	    exit()
	self.num_read += 1

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
	return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
	return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.sample()
print 'done' 
'''