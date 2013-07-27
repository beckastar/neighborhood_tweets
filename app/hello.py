from flask import Flask
from flask import render_template
app = Flask(__name__)

# import 
# #import google map api

# api = foo_api("API KEY")

@app.route("/")
def hello_world():
	return 'Hello World!'

#embed an image ... how?
@app.route("/my_map")
def my_map():
	print "This is a map"
	return render_template("map.html")

if __name__=="__main__":
	app.run(debug = True)