from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, types 
from app import db
from models import Neighborhood, Source, Content
from datetime import datetime, timedelta
import time 
import pytz
from pytz import all_timezones

utc = pytz.timezone("UTC")
pacific = pytz.timezone("US/Pacific-New")

l = []
date1 = datetime.now()
print date1
#24 hours earlier
date2 = date1-timedelta(7)
print date2



data = Content.query.filter(Content.timestamp != None).all()


dates = [] 
for d in data:
	d.timestamp =  datetime.strptime(str(d.timestamp), "%Y-%m-%d %H:%M:%S")
	if d.timestamp < date1 and d.timestamp > date2:
		dates.append(d.timestamp)

print dates





# date2=

# for d in l:
# 	if d < date1 and d> date2:
# 		l.append[d]


#trouble getting ratings out of table. 
# for d in data:
# 	d = d.split()
# 	print d


# date_today = datetime.today()
# print date_today
 
	# formatted_timestamp =  datetime.strptime(str(timestamp), "%Y-%m-%d %H:%M:%S")
	# if formatted_timestamp == date_today:
	# 	print "yes"

# 	if formatted_timestamp <_________________ and formatted_timestamp > ____________________:


 

# #standardize time format:
# timestamp = '2013-08-14 18:04:56'
# thing =  datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
# print thing





#if tweets are in the range of midnight to midnight san francisco time on yesterday's date
#
#find out if tweets are in a range 

#timestamp = 2013-08-14 18:04:56
#dt_object = datetime.strptime(timestamp, %Y-%M-%D %H:%M
#format for datetime:       
#2013, 8, 14, 16, 36, 5, 482481

#will turn twitter into datetime

# return True if timestamp is less than 24 hours ago
# then sort by timestamp
# twitter in greenwich mean time 

#<, >, = are all valid arguments 
  


# for item in content_timestamp:




# 1. datetime, message, neighborhood id copied from content
#2. updates, empties every 24 hours. 
