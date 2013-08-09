
import app 
from app import db 
from models import Content
from collections import defaultdict
#from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

 
query = db.session.query(Content).all()
#rows = db.query.statement.execute().fetchall()
print query
#d = defaultdict(int)
 

# 	print hashes
# 	d[hashes]+=1

# print d 


