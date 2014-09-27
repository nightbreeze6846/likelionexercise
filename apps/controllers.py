# -*- coding: utf-8 -*-
from flask import jsonify, render_template, request, redirect, url_for, flash, session, g
from werkzeug.security import generate_password_hash, \
	 check_password_hash
from sqlalchemy import desc
from apps import app, db
import datetime
from sqlalchemy import desc,asc
import json
from apps.forms import JoinForm, LoginForm, HistoryAddForm
from apps.models import (
	 User,
#     Video,
    History
#     Music,
#     Portfolio
)

	


@app.route('/', methods=['GET', 'POST'])
def index():
	
	if 'user_email' in session :
		user = User.query.get(session['user_email'])
		form = HistoryAddForm()
		if user.page_domain != None:
			histories = user.history.order_by(asc(History.id)).all()
			return render_template('mypage.html', user=user, form =form, histories = histories)    
		else:
			return render_template("createmypage.html",user=user)

	form = JoinForm()
	return render_template("login.html", form = form, joinModalOn='False')


@app.route('/user/join/check_email')
def check_email():
	email_input= request.args.get('email_input',"",type=str)
	user = User.query.get(email_input)
	if user != None:
		return jsonify(emailCheckPassed="False")
	else:
		return jsonify(emailCheckPassed="True")



@app.route('/user/join/', methods=['GET','POST'])
def user_join():


	form = JoinForm()
	
	
	if form.validate_on_submit():
		user = User(
			email = form.email.data,
			password = generate_password_hash(form.password.data),
			name = form.name.data,
			birthday = form.birthday.data
		)
		year=datetime.date.today().strftime("%Y")
		user.age =  int(year)-int(user.birthday.year) +1
		
		db.session.add(user)
		db.session.commit()

		session.permanent = True
		session['user_email'] = user.email
		session['user_name'] = user.name

		return redirect(url_for('index'))
	else:
		return render_template("login.html", form = form, joinModalOn='True')

@app.route('/login', methods=['POST'])
def login():
	
	email = request.form['email']
	pwd = request.form['pw']
	user = User.query.get(email)

	if user is None:
		return render_template("noemail.html")
		# flash(u'존재하지 않는 아이디, 혹은 아이디가 잘못되었습니다.', 'danger')
	elif not check_password_hash(user.password, pwd):
		return render_template("loginagain.html")
		# flash(u'비밀번호가 일치하지 않습니다.', 'danger')
	else:
		session.permanent = True
		session['user_email'] = user.email
		session['user_name'] = user.name
		flash(u'로그인 하셨습니다.', 'success')
		return redirect(url_for('index'))
	
	form = JoinForm()
	return render_template("login.html",form = form, joinModalOn='False', user=user)

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('index'))

@app.route('/changeinfo', methods=['GET', 'POST'])
def changeinfo():
	user = User.query.get(session['user_email'])
	if request.method == 'POST':
		
		newname = request.form['name']
		nowpw = request.form['pw']
		newpw = request.form['newpw']
		pwcf = request.form['pwcf']
		
		if (newpw == pwcf) and check_password_hash(user.password, nowpw) :

			user.name = newname
			user.password = generate_password_hash(newpw)

			db.session.commit()
			session.permanent = True
			session['user_name'] = user.name
			return redirect(url_for('mypage'))

		else:
			return render_template("changeinfo.html")

	return render_template("changeinfo.html", user=user)

@app.route('/memberout', methods=['GET', 'POST'])
def memberout():
	
	if request.method == "POST":
		user = User.query.get(session['user_email'])
		pwconfirm = request.form

		if check_password_hash(user.password, pwconfirm['pw']):
			
			db.session.delete(user)
			db.session.commit()
			return redirect(url_for('logout'))

	return render_template("memberout.html")

@app.route('/mypage/', methods=['GET'])
def mypage():
	user = User.query.get(session['user_email'])
	form = HistoryAddForm()
	histories = user.history.all()
	return render_template('mypage.html', user=user, form =form, histories = histories)    

@app.route('/set_domain', methods=['POST'])
def set_domain():
	if request.method == 'POST':
		user = User.query.get(session['user_email'])
		inputdom = request.form
		user.page_domain = inputdom['inputdomain']
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('createmypage.html')


@app.route('/<path:temp_domain>', methods=['GET'])
def personal_page(temp_domain=''):
	user = User.query.filter_by(page_domain=temp_domain).first()
	if user is not None:
		form = HistoryAddForm()
		if user.email == session['user_email']:
			histories = user.history.all()
			return render_template('mypage.html', user = user, form= form, histories = histories)
		else:
			histories = user.history.all()
			return render_template('personalpage.html', data = user, histories = histories)

	else: 
		return render_template('portfolio5.html')


@app.route('/save_profile', methods=['POST'])
def save_profile():
	
	
	user = User.query.get(session['user_email'])

	profile_form=request.form
	user.name = profile_form['inputname']
	user.age = profile_form['inputage']
	user.profile = profile_form['inputprofile']
	db.session.commit()
	return redirect(url_for('mypage'))

@app.route('/history/add', methods=['POST'])
def add_history():
	user = User.query.get(session['user_email'])

	form = HistoryAddForm()
	history = History(

		title = form.title.data,
		user_email = session['user_email'],
		content = form.content.data,
		tag = form.tag.data,
		starttime = form.starttime.data,
		endtime = form.endtime.data
	)
	db.session.add(history)
	db.session.commit()


	return redirect(url_for('mypage'))

@app.route('/portfolio4/', methods=['GET','POST'])
def portfolio4():
	
    if request.method == "GET":
        return render_template('portfolio4.html')    

@app.route('/portfolio5/', methods=['GET','POST'])
def portfolio5():
    if request.method == "GET":
        return render_template('portfolio5.html')    

@app.route('/portfolio6/', methods=['GET','POST'])
def portfolio6():
    if request.method == "GET":
        return render_template('portfolio6.html')    

@app.route('/portfolio7/', methods=['GET','POST'])
def portfolio7():
    if request.method == "GET":
        return render_template('portfolio7.html')    

@app.route('/portfolio8/', methods=['GET','POST'])
def portfolio8():
    if request.method == "GET":
        return render_template('portfolio8.html')   

@app.route('/Contact/', methods=['GET','POST'])
def Contact():
	
    if request.method == "GET":
        return render_template('Contact.html')     



#
# @error Handlers
#
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500
