from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, types 
from app import db
from models import Neighborhood, Source, Content
from datetime import datetime
import time 
import pytz
from pytz import all_timezones

utc = pytz.timezone("UTC")
pacific = pytz.timezone("US/Pacific-New")

#change datetime.now to utc ---- DONE
# dt = datetime.now()
# print dt
# dtutc = datetime.utcnow()
# print dtutc

#if tweets are in the range of midnight to midnight san francisco time on yesterday's date
#
#find out if tweets are in a range 

#probably need to standardize format 
#sample timestamp:2013-08-14 18:04:56
#YYYY-MM-DD HH:MM:SS 
#this is just a string. use strptime() to turn it into a datetime object

#timestamp = 2013-08-14 18:04:56
#dt_object = datetime.strptime(timestamp, %Y-%M-%D %H:%M
#format for datetime:       
#2013, 8, 14, 16, 36, 5, 482481

#will turn twitter into datetime

# return True if timestamp is less than 24 hours ago
# then sort by timestamp
# twitter in greenwich mean time 

#<, >, = are all valid arguments 

time_data = 

timestamp = '2013-08-14 18:04:56'
thing =  datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
print thing

for c in 



# for item in content_timestamp:




# 1. datetime, message, neighborhood id copied from content
#2. updates, empties every 24 hours. 
