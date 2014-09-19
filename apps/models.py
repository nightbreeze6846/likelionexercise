"""
models.py

"""
from apps import db


class User(db.Model):
    email = db.Column(db.String(255), primary_key = True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    page_domain = db.Column(db.String(255))
    subscribe = db.Column(db.Integer)
    profile = db.Column(db.String(1024))
    join_date = db.Column(db.DateTime(), default = db.func.now())


#     # relationships to models 
#     video = db.relationship('Video', backref="user", lazy='dynamic')
#     event = db.relationship('Event', backref="user", lazy='dynamic')
#     music = db.relationship('Music', backref="user", lazy='dynamic')


# class Video(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	title = db.Column(db.String(255))
# 	artist = db.Column(db.String(255))
# 	url = db.Column(db.String(255))
# 	comments = db.Column(db.String(255))
# 	User_email = db.Column(db.String(255), db.ForeignKey('user.email'))


# class Event(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	title = db.Column(db.String(255))
# 	comments = db.Column(db.String(255))
# 	# img
# 	user_email = db.Column(db.String(255), db.ForeignKey('user.email'))	

# class Music(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	title = db.Column(db.String(255))
# 	artist = db.Column(db.String(255))
# 	url = db.Column(db.String(255))
# 	album = db.Column(db.String(255))
# 	comments = db.Column(db.String(255))
# 	user_email = db.Column(db.String(255), db.ForeignKey('user.email'))	

# class Portfolio(db.Model):
# 	portfolio_domain = db.Column(db.String(255))
# 	careers = db.Column(db.String(1000))

# 	# IDs to columns
# 	video1_id = db.Column(db.Integer)
# 	video2_id = db.Column(db.Integer)
# 	video3_id = db.Column(db.Integer)
# 	video4_id = db.Column(db.Integer)
# 	video5_id = db.Column(db.Integer)

# 	music1_id = db.Column(db.Integer)
# 	music2_id = db.Column(db.Integer)
# 	music3_id = db.Column(db.Integer)
# 	music4_id = db.Column(db.Integer)
# 	music5_id = db.Column(db.Integer)

# 	event1_id = db.Column(db.Integer)
# 	event2_id = db.Column(db.Integer)
# 	event3_id = db.Column(db.Integer)
# 	event4_id = db.Column(db.Integer)
# 	event5_id = db.Column(db.Integer)

# 	User_email = db.Column(db.String(255), db.ForeignKey('user.email'))	
	
