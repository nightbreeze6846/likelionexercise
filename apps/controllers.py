# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, session, g
from werkzeug.security import generate_password_hash, \
     check_password_hash
from sqlalchemy import desc
from apps import app, db
from apps.forms import JoinForm
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
    return render_template("login.html")

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