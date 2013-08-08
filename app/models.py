
from sqlalchemy import create_engine, types 
from sqlalchemy.orm import sessionmaker
from app import db
import tweepy
import json
import pygeocoder
from pygeocoder import Geocoder
import app 
from shapely.geometry import box, Polygon, Point


consumer_key = '8vT4akwvPR1sWQIbO6y8g'
consumer_secret = '2YQxdvSVPerI51CoewMeIhyKsm8niwKZyuPIQAVg6s'
access_key= '21369282-5h31qLNIH68WoJIvfoU01DK191ixS8W9g67y41QQ'
access_secret= 'H2B6Ks97UbPs8XGxRFXNoXQpwO3Os4NTBvNi6b9B0w'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth) 
#modify to store the boundaries
#next seed 
class Neighborhood(db.Model):
	__tablename__ =  "neighborhoods"
	id = db.Column(db.Integer, primary_key= True)
	name = db.Column(db.String(64), unique = True)
	geo = db.Column(db.String(64), unique = False)
	#takes a geo tuple and tests to see which neighborhood it fits. 
	

class Source(db.Model):
	__tablename__="source"
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), unique = False)
	links = db.Column(db.String(128), unique = False)

class Content(db.Model):
	#this gets cleared every Monday
	__tablename__="content"
	id = db.Column(db.Integer, primary_key = True)
	neighborhood_id = db.Column(db.Integer, db.ForeignKey('neighborhoods.id'))
	timestamp = db.Column(db.DateTime)
	message = db.Column(db.String(280))
	hashtags = db.Column(db.String(240))
	source_id = db.Column(db.Integer, db.ForeignKey('source.id'))


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

db.create_all()