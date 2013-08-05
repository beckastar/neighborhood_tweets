from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db
#from forms import LoginForm, EditForm
#from models import User, ROLE_USER, ROLE_ADMIN
from datetime import datetime

#On front end:
#-- What am I showing? Linking visualization to databases. No need to worry right now about 
#-- ... what? What do i put here? 
# ... link to twitter.txt
#


# @lm.user_loader
# def load_user(id):
#     return User.query.get(int(id))

@app.before_request
def before_request():
    g.tweet = current_user
    #g.user = current_user
    if g.user.is_authenticated():
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.route('/')
@app.route('/index')
def index():
    user = g.user
    # posts = [
    #     { 
    #         'author': { 'nickname': 'John' }, 
    #         'body': 'Beautiful day in Portland!' 
    #     },
    #     { 
    #         'author': { 'nickname': 'Susan' }, 
    #         'body': 'The Avengers movie was so cool!' 
    #     }
    # ]
    return render_template('index.html',
        title = 'Home',
        user = user,
        posts = posts)

#@app.route('/login', methods = ['GET', 'POST'])
# @oid.loginhandler
# def login():
#     if g.user is not None and g.user.is_authenticated():
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         session['remember_me'] = form.remember_me.data
#         return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
#     return render_template('login.html', 
#         title = 'Sign In',
#         form = form,
#         providers = app.config['OPENID_PROVIDERS'])


@app.route('/edit', methods = ['GET', 'POST']) 
def edit():
    form = EditForm(g.user.nickname)
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    elif request.method != "POST":
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html',
        form = form)

@app.route('/twitterfeed')
def twitterfeed():
	return render_template("twitterfeed.html")


@app.route("/my_map")
def my_map():
	print "This is a map"
	return render_template("map.html")
 