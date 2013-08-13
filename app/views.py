from flask import render_template, flash, redirect, session, url_for 
from app import app, db 
from datetime import datetime
from flask import render_template
from models import Neighborhood, Content
from flask import jsonify
 

@app.route("/fish")
def results_json():
	cols = ['neighborhood_id']
	data = Content.query.filter(Content.neighborhood_id != None).all()

	counts = {}
	for c in data:
		if counts.get(c.neighborhood_id):
			counts[c.neighborhood_id] += 1
		else:
			counts[c.neighborhood_id] = 1

	c = jsonify(counts)
	print c
	#link key in c to neighborhood.name
	return c

@app.route("/testing")
def make_list():
	#data = Content.query(Content.neighborhood_id).all()
	data = Neighborhood.query.filter(Neighborhood.name != None).all()
	data_num = Content.query.filter(Content.neighborhood_id != None).all()
	data_dict ={} 
	for d in data:
		if data_dict.get(d.name):
			data_dict[d.name] = 1
		else:
			data_dict[d.name]=0
			#this above line here just generated all of the keys.		
	j = jsonify(data_dict)
	return j
	#this works now! put data in it. 
	# hoods = {}
	# hoods(zip(data,data_name))
	# return hoods
	# look up query examples

 
@app.route('/')
@app.route('/charts')
def hello():
	return render_template('charts.html')

if __name__ == "__main__":
    app.run()
