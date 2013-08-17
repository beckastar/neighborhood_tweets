from flask import render_template, flash, redirect, session, url_for 
from app import app, db 
from datetime import datetime
from flask import render_template
from models import Neighborhood, Content
from flask import jsonify
 
@app.route("/fish")
def results_json():
	cols = ['neighborhood_id']
	data = Content.query.filter(Content.hashtags != None).all()
	counts = {}
	for c in data:
		if counts.get(c.timestamp):
			counts[c.timestamp] += 1
		else:
			counts[c.timestamp] = 1
	c = jsonify(counts)
	return c

@app.route("/testing")
def make_list():
	thisdata = Neighborhood.query.all()
	data_dict = {} 
	for d in thisdata:
		data_dict[d.name]= d.id
	j = jsonify(data_dict)
	return j 

@app.route("/hashtags")
def hashtag_dict():
	hashdict = {}
	listofcontents = Content.query.filter(Content.hashtags !=None).all()
	for content in listofcontents:
		stringofhashes = content.hashtags
		for hashtag in stringofhashes.split():
			if hashtag not in hashdict:
				hashdict[hashtag]=1
			else:
				hashdict[hashtag] +=1
	h = jsonify(hashdict)
	return h

@app.route("/combine")
def dict_merged_tables():
	#create dictionary with the name as keys and the count as values.
	#this code produces the dictionary with the id as a key and the counter as a value.\\
	cols = ['name']
	data = Content.query.filter(Content.neighborhood_id != None).all()
	#content has neighborhood id, with neighborhood name as the foreign key
	counts = {}
	#the loop below creates a dict from content with neighborhood keys and their frequency of occurence.
	for c in data:
		if counts.get(c.neighborhood_id):
			counts[c.neighborhood_id] += 1
		else:
			counts[c.neighborhood_id] = 1
	print counts
	thisdata = Neighborhood.query.all()
	#the loop below creates a dictionary from neighborhood pairing the id and the name.
	data_dict = {} 
	for d in thisdata:
		data_dict[d.name]= d.id
	newdict = {}
	#1the loop below pairs the name with the count
	for key in data_dict:
		for k in counts:
			if data_dict[key]== k:
				newdict[key]=counts[k]
	new = jsonify(newdict)
	return new 
@app.route("/hashtags")
def hello2():
	return render_template("ratio.html")

@app.route("/ratio")
def hello1():
	return render_template("ratio.html")

@app.route('/')
@app.route('/charts')
def hello():
	return render_template('charts.html')

if __name__ == "__main__":
    app.run()
