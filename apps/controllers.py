# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, session, g
from werkzeug.security import generate_password_hash, \
	 check_password_hash
from sqlalchemy import desc
from apps import app, db
from apps.forms import JoinForm, LoginForm
from apps.models import (
	 User
#     Video,
#     Event,
#     Music,
#     Portfolio
)



# @index 

@app.route('/', methods=['GET', 'POST'])
def index():
	if 'user_email' in session :
		return render_template("portfolio3.html", username = session['user_email'])
	return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
	
	email = request.form['email']
	pwd = request.form['pw']    
	user = User.query.get(email)

	if user is None:
		flash(u'존재하지 않는 아이디, 혹은 아이디가 잘못되었습니다.', 'danger')
	elif not check_password_hash(user.password, pwd):
		flash(u'비밀번호가 일치하지 않습니다.', 'danger')
	else:
		session.permanent = True
		session['user_email'] = user.email
		session['user_name'] = user.name
		flash(u'로그인 하셨습니다.', 'success')
		return redirect(url_for('index'))
	
	return render_template("login.html")

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('index'))

@app.route('/changeinfo', methods=['GET', 'POST'])
def changeinfo():
	info = User.query.get(session['user_email'])

	if request.method == 'POST':
		newinfo = request.form
		info.name = newinfo['name']
		if newinfo['pw'] == newinfo['pwcf']:
			info.password = newinfo['pw']

			db.session.commit()
			return redirect(url_for('index'))

		else:
			return render_template("update_profile.html")

	return render_template("changeinfo.html")

@app.route('/memberout', methods=['GET', 'POST'])
def memberout():
	
	if request.method == "POST":
		mem = User.query.get(session['user_email'])
		pwconfirm = request.form
		if check_password_hash(mem.password, pwconfirm['pw']):
			
			db.session.delete(mem)
			db.session.commit()
			
			return redirect(url_for('logout'))

	return render_template("memberout.html")


@app.route('/user/join/', methods=['GET','POST'])
def user_join():
	form = JoinForm()

	if request.method == "POST":
		if form.validate_on_submit():
			user = User(
				email = form.email.data,
				password = generate_password_hash(form.password.data),
				name = form.name.data
			)
			db.session.add(user)
			db.session.commit()
			
			return redirect(url_for('index'))
	else :
		return render_template('/user/join.html', form=form)



@app.route('/user/make_profile/', methods=['GET','POST'])
def update_profile():
	if request.method == "GET":
		return render_template('/user/update_profile.html')
 
@app.route('/portfolio3/', methods=['GET','POST'])
def portfolio3():
	if request.method == "GET":
		return render_template('portfolio3.html')    

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
