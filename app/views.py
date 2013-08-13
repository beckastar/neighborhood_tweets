from flask import render_template, flash, redirect, session, url_for 
from app import app, db 
from datetime import datetime
from flask import render_template
from models import Neighborhood, Content
from flask import jsonify
 

# @app.before_request
# def before_request(): 
# @app.errorhandler(404)
# def internal_error(error):
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_error(error):
#     db.session.rollback()
#     return render_template('500.html'), 500

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

	# result = [{col:getattr(d, col) for col in cols} for d in data]
	c = jsonify(counts)
	# l = []
	# for k, v in c:
	# 	l.append[(k, d[k])] 
	return c
 

#next step: get google charts to take in data. look up jinja 

@app.route('/')
@app.route('/charts')
def hello():
	return render_template('charts.html')


# @app.route('/layout')
# def layouts():
# 	return render_template()

     
 
 
#  if __name__ == '__main__':
# 	# Automatically detect changes to charts.py and reload the server as
# 	# necessary.
# 	app.run(debug=True)

if __name__ == "__main__":
    app.run()
