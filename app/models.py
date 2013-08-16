
from sqlalchemy import create_engine, types 
from sqlalchemy.orm import sessionmaker
from app import db 
import json  
import app  

TWITTER_SOURCE_ID = 1

class Neighborhood(db.Model):
	__tablename__ =  "neighborhoods"
	id = db.Column(db.Integer, primary_key= True)
	south_lat =  db.Column(db.DECIMAL, unique=False)
	west_long = db.Column(db.DECIMAL, unique=False)
	north_lat = db.Column(db.DECIMAL, unique=False)
	east_long = db.Column(db.DECIMAL, unique=False)
	name = db.Column(db.String(64), unique = True) 

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

class Ratings_7day(db.Model):
	__tablename__="rating7"
	id = db.Column(db.Integer, primary_key = True)
	neighborhood_id = db.Column(db.Integer, db.ForeignKey('content.neighborhood_id'))
	timestamp = db.Column(db.DateTime, db.ForeignKey('content.timestamp'))

class SF_Tweets(db.Model):
	__tablename__ = "all_sf"
	id = db.Column(db.Integer, primary_key = True)
	hashtags = db.Column(db.String(240))
	timestamp = db.Column(db.DateTime)
	message = db.Column(db.String(280))
	geo = db.Column(db.Integer)


#create Ratings_7day in sqlite3

db.create_all()
