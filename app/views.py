from flask import render_template, flash, redirect, session, url_for 
from app import app, db 
from datetime import datetime
from flask import render_template
from models import Neighborhood, Content
from flask import jsonify 
import re
import nltk 
from nltk import bigrams
import unicodedata
import json


# @app.route("/fish")
# def results_json():
# 	cols = ['neighborhood_id']
# 	data = Content.query.filter(Content.hashtags != None).all()
# 	counts = {}
# 	for c in data:
# 		if counts.get(c.timestamp):
# 			counts[c.timestamp] += 1
# 		else:
# 			counts[c.timestamp] = 1
# 	c = jsonify(counts)
# 	return c

# @app.route("/testing")
# def make_list():
# 	thisdata = Neighborhood.query.all()
# 	data_dict = {} 
# 	for d in thisdata:
# 		data_dict[d.name]= d.id
# 	j = jsonify(data_dict)
# 	return j 
 
def transform(word):
	word = word.lower()
	punctuation = ".,;:@!.()_#1-+$?^/23456'7890]\&["
	while word and word[0] in punctuation:
		word = word[1:]
	while word and word[-1] in punctuation:
		word = word[:-1]
	list_of_words = ["sfo","...","restaurant","not","location" ,"hotel" ,"se","f","venta","ya","yo","su","un","vamos","really","sf","s","para","st","linkedin's","seguridad","diputado","arroyo","los","al","cat","lo","founder","introduces","drops","bathroom","coffee","llega","llegar","cafe","degrees","photo","","tells","building","street","y","beautiful","app","beach","today","jose","hp","edition","por", "favorite","cofee","chance", "agency","area","heart","heart","eparegion","ers","center","check", "can't","vs","bambu","boletos","airport","bridge","boletas",  "que","processar","q","am","pm","partido","park","open","online","next","news","mede","looking","lol","las","ht","jueves", "international","its","into","in","i","going","hq","hoy","golden","gate","faltes","este","es","desde", "con","d","b","el","la","del", "others","en","abc7newsbayarea","chronicle","chubby","checker","cogita","at&amp;t","agosto","being","amp","best","california","ca", "sanfrancisco","francisco","th", "the","rt","bro", "o","\u2026","via","w","a","bay","ca","francisco's","it's","m\u00fasico","p\u00eanis","quer","plaza","la", "francisco", "i'll","i'm", "de", "san", "ca", "fran", "city" "the","name","of","very","to","through","and","just","a","form","in","much","is","great","it","think","you","say","that","help","he","low","was","line","for","before","on","turn","are","cause","with","same","as","mean","I","differ","his","move","they","right","be","boy","at","old","one","too","have","does","this","tell","from","sentence","or","set","had","three","by","want","hot","air","but","well","some","also","what","play","there","small","we","end","can","put","out","home","other","read","were","hand","all","port","your","large","when","spell","up","add","use","even","word","land","how","here","said","must","an","big","each","high","she","such","which","follow","do","act","their","why","time","ask","if","men","will","change","way","went","about","light","many","kind","then","off","them","need","would","house","write","picture","like","try","so","us","these","again","her","animal","long","point","make","mother","thing","world","see","near","him","build","two","self","has","earth","look","father","more","head","day","stand","could","own","go","page","come","should","did","country","my","found","sound","answer","no","school","most","grow","number","study","who","still","over","learn","know","plant","water","cover","than","food","call","sun","first","four","people","thought","may","let","down","keep","side","eye","been","never","now","last","find","door","any","between","new","city","work","tree","part","cross","take","since","get","hard","place","start","made","might","live","story","where","saw","after","far","back","sea","little","draw","only","left","round","late","man","run","year","don't","came","while","show","press","every","close","good","night","me","real","give","life","our","few","under","stop"]
	if word.startswith("http"):
		return 
	if word.startswith("https"):
		return 
	if word.startswith( "\u201c"):
		return
	if word.startswith("\u"):
		return
	if word in list_of_words:
		return
	return word

@app.route("/worddict")
def word_dict():
	worddict = {}
	display = {}
	#relative frequency
	listofcontents = Content.query.all()
	for content in listofcontents:
		stringofwords = content.message

		if not stringofwords:
			continue
		for word in stringofwords.split():
			word = transform(word)
			if word is None:
				continue
			if word not in worddict:
				worddict[word]=1
			else:
				worddict[word] += 1

	for word in worddict:
		if worddict[word] >4:
			display[word] = worddict[word]

	return jsonify(display)

@app.route("/wordarray")
def word_array():
	wordarray = []
	countingdict = {}
	otherarray=[]
	#relative frequency
	listofcontents = Content.query.all()
	for content in listofcontents:
		stringofwords = content.message
		if not stringofwords:
			continue
		for word in stringofwords.split():
			word = transform(word)
			if word is None:
				continue
			wordarray.append([word, ""])
	for word in wordarray:
		if countingdict.get(word[0]):
			countingdict[word[0]] += 1
		else:
			countingdict[word[0]] =1
	i = 0
	for k in countingdict:
		while i<=countingdict[k]:
			otherarray.append([k,""])
			i+=1
	print otherarray					
	#chuck things out at this point
	#print countingdict
	return json.dumps(otherarray)

@app.route("/combine")
def dict_merged_tables(): 
	cols = ['name']
	data = Content.query.filter(Content.neighborhood_id != None).all() 
	counts = {} 
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
	#the loop below pairs the name with the count
	for key in data_dict:
		for k in counts:
			if data_dict[key]== k:
				newdict[key]=counts[k]
	new = jsonify(newdict)
	return new 

@app.route("/geotagged_ratio")
def find_privacy(): 
	id_counts = 0
	no_id_counts = 0
	d = {}
	listofcontents = Content.query.all()
	for content in listofcontents:
		c = content.neighborhood_id
		if c:
			id_counts +=1	
		else:
			no_id_counts +=1
	#d["this is a thing"] = 17
	d["Tagged"]= id_counts
	d["Secret Location"] = no_id_counts
	d["Geotagged"] = id_counts
	jd = jsonify(d)
	return jd

 
# @app.route("/bigrams")
# def find_word_pairs():
# 	data = Content.query.all() 
# 	punctuation = ".,;:@!.()_#1-+$?^/23456'7890]\&["
# 	bigram = {}
# 	for content in data:
# 		words = content.message
# 		if not words:
# 			continue
# 		words = unicodedata.normalize('NFKD', words).encode('ascii','ignore')
# 		tokens  = words.split()
# 	bigs= bigrams(tokens)
# 	for pair in bigs:
# 		if bigram.get(pair):
# 			bigram[pair] +=1
# 		else:
# 			bigram[pair] = 1
# 	jasbig = jsonify(bigram)
# 	return jasbig


@app.route("/bigrams")
def find_word_pairs():
	data = Content.query.all() 
	list_of_words = ["sfo","...","restaurant","not","location" ,"hotel" ,"se","f","venta","ya","yo","su","un","vamos","really","sf","s","para","st","linkedin's","seguridad","diputado","arroyo","los","al","cat","lo","founder","introduces","drops","bathroom","coffee","llega","llegar","cafe","degrees","photo","","tells","building","street","y","beautiful","app","beach","today","jose","hp","edition","por", "favorite","cofee","chance", "agency","area","heart","heart","eparegion","ers","center","check", "can't","vs","bambu","boletos","airport","bridge","boletas",  "que","processar","q","am","pm","partido","park","open","online","next","news","mede","looking","lol","las","ht","jueves", "international","its","into","in","i","going","hq","hoy","golden","gate","faltes","este","es","desde", "con","d","b","el","la","del", "others","en","abc7newsbayarea","chronicle","chubby","checker","cogita","at&amp;t","agosto","being","amp","best","california","ca", "sanfrancisco","francisco","th", "the","rt","bro", "o","\u2026","via","w","a","bay","ca","francisco's","it's","m\u00fasico","p\u00eanis","quer","plaza","la", "francisco", "i'll","i'm", "de", "san", "ca", "fran", "city" "the","name","of","very","to","through","and","just","a","form","in","much","is","great","it","think","you","say","that","help","he","low","was","line","for","before","on","turn","are","cause","with","same","as","mean","I","differ","his","move","they","right","be","boy","at","old","one","too","have","does","this","tell","from","sentence","or","set","had","three","by","want","hot","air","but","well","some","also","what","play","there","small","we","end","can","put","out","home","other","read","were","hand","all","port","your","large","when","spell","up","add","use","even","word","land","how","here","said","must","an","big","each","high","she","such","which","follow","do","act","their","why","time","ask","if","men","will","change","way","went","about","light","many","kind","then","off","them","need","would","house","write","picture","like","try","so","us","these","again","her","animal","long","point","make","mother","thing","world","see","near","him","build","two","self","has","earth","look","father","more","head","day","stand","could","own","go","page","come","should","did","country","my","found","sound","answer","no","school","most","grow","number","study","who","still","over","learn","know","plant","water","cover","than","food","call","sun","first","four","people","thought","may","let","down","keep","side","eye","been","never","now","last","find","door","any","between","new","city","work","tree","part","cross","take","since","get","hard","place","start","made","might","live","story","where","saw","after","far","back","sea","little","draw","only","left","round","late","man","run","year","don't","came","while","show","press","every","close","good","night","me","real","give","life","our","few","under","stop"]
	punctuation = ".,;:@!.()_#1-+$?^/23456'7890]\&["
	bigr= {}
	for content in data:
		words = content.message
		if words:
			words = words.encode('ascii','ignore')
			tokens = words.split()
			bigs = bigrams(tokens)
			for tup in bigs:
				if bigr.get(tup):
					bigr[tup] +=1
				else:
					bigr[tup] = 1
   	return str(bigr)
	# jasbig =jsonify(bigram)
	# return jasbig


# @app.route("/just_now")

# @app.route("/yesterday")
# def yesterday():


@app.route('/')
@app.route('/charts')
def hello():
	return render_template('charts.html')

if __name__ == "__main__":
    app.run()
