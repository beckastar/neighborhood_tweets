
import app 
from app import db 
from models import Content
from collections import defaultdict 
from sqlalchemy.sql import select

 
# query_hashtags = db.session.query(Content.hashtags).all() 
# print query_hashtags

query_neighborhoods = db.session.query(Content.neighborhood_id).all()
print query_neighborhoods

# #sort hashtags
# d_hashtags = defaultdict(int)
# for tuples in query:
# 	for s in tuples: 
# 		if not s:
# 			continue
# 		words = s.split("#")
# 		words = words[1:]
# 		for word in words:
# 			d_hashtags[word] += 1
# import pprint
# pprint.pprint (dict(d_hashtags)) 

#sort neighborhoods

# d_neighborhoods = defaultdict(int)




# pprint.pprint = defaultdict(int)
#sort sentiments




