from flask import render_template, flash, redirect, session, url_for 
from app import app, db 
from datetime import datetime
from flask import render_template
from models import Neighborhood, Content

 

# @app.before_request
# def before_request(): 
# @app.errorhandler(404)
# def internal_error(error):
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_error(error):
#     db.session.rollback()
#     return render_template('500.html'), 500

@app.route('/')
def index(): 
        #return render_template("index.html")
		data = [('Western Addition', 11), ('Upper Haight', 30), ('Potrero', 15), ('Dogpatch', 42),
			('Pacific Heights', 38), ('Fillmore', 45), ('Cole Valley', 52)]
		return render_template('index.html', data=data)
       

@app.route('/chart/') 
def hello():
	return 

@app.route('/layout/')
def layouts():
	return render_template()

     

# @app.route('/twitterfeed')
# def twitterfeed():
# 	return render_template("twitterfeed.html", 
# 		title = "test")


# @app.route("/my_map")
# def my_map():
# 	print "This is a map"
# 	return render_template("map.html")
 
#  if __name__ == '__main__':
# 	# Automatically detect changes to charts.py and reload the server as
# 	# necessary.
# 	app.run(debug=True)

if __name__ == "__main__":
    app.run()
