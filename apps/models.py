"""
models.py

"""
from apps import db

#
# add User Model
#
class User(db.Model):
    email = db.Column(db.String(255), primary_key = True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    join_date = db.Column(db.DateTime(), default = db.func.now())
    page_domain = db.Column(db.String(255))
    subscribe = db.Column(db.Integer)



    # 일대다 관계를 가진 비디오, 음원 등을 관계 설정
    video = db.relationship('Video', backref="user", lazy='dynamic')
    event = db.relationship('Event', backref="user", lazy='dynamic')
    music = db.relationship('Music', backref="user", lazy='dynamic')


class Video(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(255))
	artist = db.Column(db.String(255))
	url = db.Column(db.String(255))
	comments = db.Column(db.String(255))
	User_email = db.Column(db.String(255), db.ForeignKey('user.email'))


class Event(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(255))
	comments = db.Column(db.String(255))
	# img
	user_email = db.Column(db.String(255), db.ForeignKey('user.email'))	

class Music(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(255))
	artist = db.Column(db.String(255))
	url = db.Column(db.String(255))
	album = db.Column(db.String(255))
	comments = db.Column(db.String(255))
	user_email = db.Column(db.String(255), db.ForeignKey('user.email'))	

class Portfolio(db.Model):
	portfolio_domain = db.Column(db.String(255))
	careers = db.Column(db.String(1000))

	# 각 항목들에 대한 ID
	video1_id = db.Column(db.Integer)
	video2_id = db.Column(db.Integer)
	video3_id = db.Column(db.Integer)
	video4_id = db.Column(db.Integer)
	video5_id = db.Column(db.Integer)

	music1_id = db.Column(db.Integer)
	music2_id = db.Column(db.Integer)
	music3_id = db.Column(db.Integer)
	music4_id = db.Column(db.Integer)
	music5_id = db.Column(db.Integer)

	event1_id = db.Column(db.Integer)
	event2_id = db.Column(db.Integer)
	event3_id = db.Column(db.Integer)
	event4_id = db.Column(db.Integer)
	event5_id = db.Column(db.Integer)

	User_email = db.Column(db.String(255), db.ForeignKey('user.email'))	
	
