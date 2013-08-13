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
	return c

@app.route("/testing")
def make_list():
	thisdata = Neighborhood.query.all()
	data_dict = {} 
	for d in thisdata:
		data_dict[d.name]= d.id
	j = jsonify(data_dict)
	return j

@app.route('/')
@app.route('/charts')
def hello():
	return render_template('charts.html')

if __name__ == "__main__":
    app.run()
