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


class PrivatePage(db.Model):
	user_id = db.Column(db.String(255), db.ForeignKey('user.id'))
	# Foreign key
	email = db.Column(db.String(255), primary_key = True)
	music = db.Column(db.)