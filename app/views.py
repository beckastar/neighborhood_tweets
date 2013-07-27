from flask import render_template, Flask, request, url_for, flash, g
from flask_oauth import OAuth
import twitter
from flask import session
from flask import redirect
from app import app
#views should only be routes - put twitter setup 

# oauth = OAuth()
#oauth.init

def get_id(self):
	return self.id

def is_authenticated(self):
	return True

def is_active(self):
	return True

def is_anonymous(self):
	return False


@app.route("/")
@app.route("/index")
def index():
	user = {'nickname': 'Miguel'}#fake user
	return render_template('index.html',
		return '''
		<html>
		<head>
		<title>Home  Page</title>
		<body>
		<h1>Hello, '''+user['nickname']+'''</h1>
		</body>
		</html>
		'''
		 

@app.route('/twitterfeed')
def twitterfeed():
	return render_template("twitterfeed.html")


@app.route("/my_map")
def my_map():
	print "This is a map"
	return render_template("map.html")

#start with public tweets 
# @app.route("/login")
# def login():
# 	if current_user.is_authenticated:
# 		return redirect("/")
# 	return twitter.authorize(callback=url_for("oauth_authorized",
# 		next=request.args.get('next') or request.referrer or None))

# @twitter.tokengetter
# def get_twitter_token(token=None):
# 	return session.get('twitter_token')

# @app.route("/twitterfeed", methods = [GET ])
# 	return render_template("twitters.html")

