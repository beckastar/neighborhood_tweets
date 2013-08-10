
import app 
from app import db 
from models import Content
from collections import defaultdict
#from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

 
query = db.session.query(Content.hashtags).all()
#rows = db.query.statement.execute().fetchall()

print query

d = defaultdict(int)
for tuples in query:
	# print tuples
	for s in tuples:
		# s is a string, e..g "#hashtag#another"
		if not s:
			continue
		words = s.split("#")
		words = words[1:]
		for word in words:
			d[word] += 1
import pprint
pprint.pprint (dict(d))

			# print "THESE ARE WORDS", words
			# print len(words)
			# for item in words:
			# 	item = str(item)
			# 	if item not in d.values():
			# 		d[item] = 1
			# 	else:
			# 		d[item] +=1
			# # d[s] += len(words)
			# elif '#' in word:
			# 	l.append(word)
			# for letter in word:
			# 	if letter == None:
			# 		continue
			# 	elif letter == "#":
			# 		word = word.split("#")
			# 		word = str(word)
		 # 				l.append("#")
		 # 				d[word]+=1
# print l
# print "THIS IS YOUR DICTIONARY",d



# for word in l:
# 	
# print d 


