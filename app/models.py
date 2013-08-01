#by Saturday:
#get content and store into content table
#run and leave it running 
#My code - match against 

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, types 
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, scoped_session 	
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
import json
import datetime
from app import db 

ROLE_USER = 0
ROLE_ADMIN = 1

class Neighborhood(db.Model):
	id = db.Column(db.Integer, primary_key= True)
	name = db.Column(db.String(64), unique = True)
	geo = db.Column(db.String(64), unique = False)

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