
import app 
from app import db 
from models import Content
from collections import defaultdict
#from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

 
query = db.session.query(Content.hashtags).all()
#rows = db.query.statement.execute().fetchall()

print query

print query

# d = defaultdict(int)
l =[]
for tuples in query:
	for letter in tuples:
		print tuples
		for word in tuples:
			if word == None:
				continue
			elif '#' in word:
				word = word.split("#")
				l.append(word)
			# for letter in word:
			# 	if letter == None:
			# 		continue
			# 	elif letter == "#":
	 	# 			l.append("#")
print l


# 	print hashes
# 	d[hashes]+=1

# print d 


