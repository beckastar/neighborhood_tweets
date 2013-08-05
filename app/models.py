
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, types 
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, scoped_session 	
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
import json
import datetime
from app import db 
import twitterlisten


ROLE_USER = 0
ROLE_ADMIN = 1

class Neighborhood(db.Model):
	__tablename__ =  "neighborhoods"
	id = db.Column(db.Integer, primary_key= True)
	name = db.Column(db.String(64), unique = True)
	geo = db.Column(db.String(64), unique = False)
	#takes a geo tuple and tests to see which neighborhood it fits. 

class Source(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), unique = False)
	links = db.Column(db.String(128), unique = False)

class Content(db.Model):
#this gets cleared every Monday
	id = db.Column(db.Integer, primary_key = True)
	neighborhood_id = db.Column(db.Integer, db.ForeignKey('neighborhood.id'))
	timestamp = db.Column(db.DateTime)
	message = db.Column(db.String(280))
	hashtags = db.Column(db.String(240))
	source_id = db.Column(db.Integer, db.ForeignKey('source.id'))

def point_in_neighborhood(x,y,poly): 
#test if point in polygon 
    



    #process geodata to determine where it is based on 
    #define custome method to filter lat long into neighborhood

# import sys
# import tweepy
# import json
# from tweepy.streaming import StreamListener
# from tweepy import Stream 
# from tweepy import OAuthHandler 
# import pygeocoder
# from pygeocoder import Geocoder
# import app 
# #from models import Neighborhood, Source, Content as db_session
# from shapely.geometry import Polygon
# #Ratings_24, Ratings_7day, Ratings_month, Ratings_year 

# consumer_key = '8vT4akwvPR1sWQIbO6y8g'
# consumer_secret = '2YQxdvSVPerI51CoewMeIhyKsm8niwKZyuPIQAVg6s'
# access_key= '21369282-5h31qLNIH68WoJIvfoU01DK191ixS8W9g67y41QQ'
# access_secret= 'H2B6Ks97UbPs8XGxRFXNoXQpwO3Os4NTBvNi6b9B0w'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_key, access_secret)

# api = tweepy.API(auth)
# #query - opening connecting 

# def bs(obj): #to_byte_string
#     if isinstance(obj, str):
#         return obj
#     elif isinstance(obj, unicode):
#         return obj.encode('utf-8')
#     else:
#         return obj


# for tweet in tweepy.Cursor(api.search, q='san francisco').items(100):
#     #
#     if tweet.coordinates :
#         #import pdb;pdb.set_trace()
#         print bs(tweet.text), bs(tweet.created_at), bs(tweet.coordinates)
#         coordinates = tweet.coordinates['coordinates']
#         #print coordinates
# #       print gmaps.latlng_to_address(coordinates[0], coordinates[1])
#         #store into database
#         print bs("Geocoding: %r, %r" % (coordinates[0],coordinates[1]))
#         results= Geocoder.reverse_geocode(coordinates[1],coordinates[0])
#         print bs("Results: %s" % results)
#         print "\n"

# #define neighborhoods by geo (use pygeocoder)now just doing squares, will upgrade later...

# Upper_Haight = Neighborhood()
#     #Stanyan and Oak
# Upper_Haight.borders =(Polygon(
#     (37.771034, -122.453849),
#     #Stanyan and Waller:
#     (37.768269, -122.453334),
#     #Divis and Waller
#     (37.770373, -122.436790)
#     #Divis and Oak
#     (37.773154, -122.437391)
#     )
#     )

# point = (37.774223, -122.444429)

# if point.within(Upper_Haight.borders):
#     print "yes yes yes"

# if Upper_Haight.point_in_neighborhood(x, y, point

# class Ratings_24():
# #aggregating data from Content for display
# #this gets cleared once a week


# class Ratings_7day():
# #aggregating data from ratings_24 for display
# #this gets cleared every Monday


# class Ratings_month():
# #aggreagting data from ratings_7day for display
# #this doesn't get cleared



# class Ratings_year():
# #this doesn't get cleared


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     nickname = db.Column(db.String(64), unique = True)
#     email = db.Column(db.String(120), index = True, unique = True)
#     role = db.Column(db.SmallInteger, default = ROLE_USER)
#     posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
#     about_me = db.Column(db.String(140))
#     last_seen = db.Column(db.DateTime)
#     followed = db.relationship('User', 
#         secondary = followers, 
#         primaryjoin = (followers.c.follower_id == id), 
#         secondaryjoin = (followers.c.followed_id == id), 
#         backref = db.backref('followers', lazy = 'dynamic'), 
#         lazy = 'dynamic')

#     @staticmethod
#     def make_unique_nickname(nickname):
#         if User.query.filter_by(nickname = nickname).first() == None:
#             return nickname
#         version = 2
#         while True:
#             new_nickname = nickname + str(version)
#             if User.query.filter_by(nickname = new_nickname).first() == None:
#                 break
#             version += 1
#         return new_nickname


# 	def is_authenitcated(self):
# 		return True

# 	def is_active(self):
# 		return True

# 	def is_anonymous(self):
# 		return False

# 	def get_id(self):
# 		return unicode(self.id)

#     def avatar(self, size):
#         return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)
        
#     def __repr__(self):
#         return '<User %r>' % (self.nickname)   
# class Post(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	body = db.Column(db.String(140))
# 	timestamp = db.Column(db.DateTime)
# 	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# 	def __repr__(self):
# 		return '<Post %r>' %(self.body)

# followers =db.Table('followers',
# 	db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
# 	db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
# 	)