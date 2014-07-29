# -*- coding: utf-8 -*-
# all the imports

from flask import request, redirect, url_for,\
    render_template
from apps import app
from database import Database
from google.appengine.ext import db
from datetime import datetime

class Photo(db.Model):
	photo = db.BlobProperty()

def allowed_file(filename):
	ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

	return '.' in filename and \
	filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

dataStorage = Database()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def show_posts():
    posts = dataStorage.out()
    return render_template('show_posts.html', posts=posts)


@app.route('/add', methods=['POST'])

def add_post():
	# storage == post
	# putting data into storage variable
	storage={}
	storage['author'] = request.form['author']
	storage['contents'] = request.form['contents']
	storage['date'] = datetime.now().strftime('%Y-%m-%d %H:%M')

	# read photo file from request
	post_data = request.files['photo']
	if post_data and allowed_file(post_data.filename):
		filestream = post_data.read()
		# upload on google app engine db
		upload_data = Photo()
		upload_data.photo = db.Blob(filestream)
		upload_data.put()
	# putting photo's key(defined in gae) into storage
	storage['photo'] = upload_data.key()
	dataStorage.put(storage)
	return redirect(url_for('show_posts'))


@app.route('/show/<key>')
def shows(key):
	uploaded_data = db.get(key)
	return app.response_class(uploaded_data.photo)