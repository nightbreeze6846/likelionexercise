# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, session, g
from werkzeug.security import generate_password_hash, \
     check_password_hash
from sqlalchemy import desc
from apps import app, db
from apps.forms import JoinForm
from apps.models import (
    User
)
import pusher

#
# @index 
#
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user_email' in session :

        return render_template("chat.html")        
    return render_template("login.html",message="")

@app.route('/send', methods=['GET'])    
def sendmsg():
    p = pusher.Pusher(
        app_id='86616',
        key='69ea7e9cd25b0aa6ff1c',
        secret='6e11a0924988a1f07d57'
    )

    
    chat_msg = request.args.get('msg_data')
    p['test_channel'].trigger('event_msg', {'name': session['user_name'], 'msg' : chat_msg})
    return ""


# @Join controllers

@app.route('/user/join/', methods=['GET', 'POST'])
def user_join():
    form = JoinForm()   

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(
                email=form.email.data,
                password=generate_password_hash(form.password.data),
                name=form.name.data
            )

            db.session.add(user)
            db.session.commit()

            return redirect(url_for('index'))
    else:
        return render_template('/user/join.html', form=form)


@app.route('/login/', methods=['POST'])
def login():

    email = request.form['email']
    pw = request.form['pw']

    user = User.query.get(email)
    message = None

    if user is None:
        message = u"user가 존재하지 않습니다."
    elif not check_password_hash(user.password,pw):
        message = u"password가 잘못되었습니다."
    else:
        p = pusher.Pusher(
            app_id='86616',
            key='69ea7e9cd25b0aa6ff1c',
            secret='6e11a0924988a1f07d57'
        )

        session.permanent = True
        session['user_email'] = user.email
        session['user_name'] = user.name

        # 로그인 메세지 뿌리기
        p['test_channel'].trigger('login_msg', {'name': user.name})
        return redirect(url_for('index'))

    return render_template("login.html",message=message)



@app.route('/logout')
def logout():
    p = pusher.Pusher(
        app_id='86616',
        key='69ea7e9cd25b0aa6ff1c',
        secret='6e11a0924988a1f07d57'
    )
    name = session['user_name']
    session.clear()
    
    # 로그아웃 메세지 뿌리기
    p['test_channel'].trigger('logout_msg', {'name': name})
    return redirect(url_for('index'))

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