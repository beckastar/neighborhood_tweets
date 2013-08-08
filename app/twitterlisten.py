#REMINDER IF YOU PUT THE FLASK MEGA TUTORIAL CODE IN HERE, YOU'RE GOING TO BE SAD

import sys
import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import Stream 
from tweepy import OAuthHandler 
# import pygeocoder
# from pygeocoder import Geocoder
import app 
from app import db
import models
from models import Neighborhood, Source, Content
from shapely.geometry import Polygon, Point 
from decimal import *
import traceback

#Ratings_24, Ratings_7day, Ratings_month, Ratings_year 
content = Content()
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

for tweet in tweepy.Cursor(api.search, q='san francisco').items(200):
    if tweet.coordinates :
        print bs(tweet.text), bs(tweet.created_at), (tweet.coordinates)
        tweets = bs(tweet.text)
        tweetwhen = bs(tweet.created_at)
        s = tweets.split()
        tags = set()
        for word in s:
        		if word.startswith("#"):
        			tags.add(bs(word))
        			print word  
        # print "json object coordinates", tweet.coordinates['coordinates'][0][1]
        lat = tweet.coordinates["coordinates"][0]
        lon = tweet.coordinates["coordinates"][1]
        # print "lon", type(lon)
        # print "lat",lat 
        # print 'lon', lon
        # latlong = Point(lat,lon)
        # print "this is point",latlong
        neighborhoods=db.session.query(Neighborhood).all()
       
        # print "coords",coords[0]
        # print "type", type(coords[0])
        # x = Decimal(coords[0])
        # print "type x", type(x)
        # for item in coords:
        #     print item 
        #     item = Decimal(item)
        #     print item, type(item)   
        for neighborhood in neighborhoods:
            print "hi", neighborhood.geo
            coords = neighborhood.geo.split(',')
            print "this is neighborhood geo", neighborhood.geo
            # neighborhood.geo = neighborhood.geo.split()
            print "this is neighborhood geo split", neighborhood.geo
            print "neighborhood.geo typei", type(neighborhood.geo)

            #THIS IS A STRING... PARSE ME!!!!!!
            x = neighborhood.geo[0]

            #PARSE ME STARTER GUIDE

            # neighborhood.geo[0]=unicodedata.numeric(neighborhood.geo[0])
            # print "neighborhood.geo typei [0]", type(neighborhood.geo[0]), neighborhood.geo[0]

            square = () 
                # latlongs = float(latlongs)
                
                # square.add(latlongs)
                # print square 

        #     if latlong.within((neighborhood.geo)):
        #         content.id = neighborhood.id
        print type(tweets)
        print tweets
        content.message = tweets
        content.timestamp = tweetwhen
        content.hashtags = " ".join(tags)
        #create instance of content class 
        try:
 #       	db.session.add(neighborhoods)
	        db.session.add(content)
	        db.session.commit()
    	except Exception, e:
    		# print "Unicode error."
    		traceback.print_exc()




