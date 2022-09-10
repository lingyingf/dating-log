"""Data Models for dating log app."""

from flask_sqlalchemy import SQLAlchemy
import datetime

from sqlalchemy import false

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()


def connect_to_db(flask_app, db_uri="postgresql:///logs", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = False
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


class User (db.Model):
    """"create user table """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    log_ref = db.relationship("Log", back_populates = "user_ref")
    friend_ref = db.relationship("Friend", back_populates = "user_ref")
    comment_ref = db.relationship("Comment", back_populates = "user_ref")

    def __repr__(self):
        return f'<User user_id={self.user_id} user_name={self.user_name} email={self.email}>'



class Log (db.Model):
    """create edit log"""

    __tablename__ = "logs"

    log_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    first_name_dated = db.Column(db.String, nullable=False)
    last_name_dated = db.Column(db.String)
    date_of_the_date = db.Column(db.DateTime)
    city_met = db.Column(db.String)
    overall_rating = db.Column(db.Integer, nullable=False)
    app_met = db.Column(db.String)
    key_takeaway = db.Column(db.String)
    description = db.Column(db.String)
    contact_info = db.Column(db.String)
    picture = db.Column(db.String)
    sharing = db.Column(db.String)

    user_ref = db.relationship("User", back_populates = "log_ref")
    comment_ref = db.relationship("Comment", back_populates = "log_ref")

    def __repr__(self):
        return f'<Log log_id ={self.log_id} user_id={self.user_id} date_of_the_date={self.date_of_the_date}>'


class Friend (db.Model):
    """create friend list"""

    __tablename__ = "friends"

    friend_edit_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_email = db.Column(db.String, db.ForeignKey("users.email"), nullable=False)
    friend_email = db.Column(db.String, nullable=False)
    friend_username = db.Column(db.String, nullable=False)

    user_ref = db.relationship("User", back_populates = "friend_ref")

    def __repr__(self):
        return f'<Friend friend_id ={self.friend_edit_id} user_email={self.user_email} friend_email={self.friend_email}>'


class Comment (db.Model):
    """create comment for the log"""

    __tablename__ = "comments"

    comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    commentor_email = db.Column(db.String, db.ForeignKey("users.email"), nullable=False)
    log_id = db.Column(db.Integer, db.ForeignKey("logs.log_id"), nullable=False)
    comments = db.Column(db.String)
    comment_create_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    user_ref = db.relationship("User", back_populates = "comment_ref")
    log_ref = db.relationship("Log", back_populates = "comment_ref")

    def __repr__(self):
        return f'<Comment comment_id ={self.comment_id} commentor_email={self.commentor_email} log_id={self.log_id} comment_create_time={self.comment_create_time}>'




if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)