"""CRUD operations."""

from model import Friend, db, User, Log, Comment, connect_to_db
import datetime





# create get user_email by email

def get_user_by_email(email):
    """Return a user email by email."""

    return User.query.filter(User.email == email).first()



# insert the user data into the database

def insert_new_user(user_name, email, password):
    """Insert the data into the User database"""

    new_user = User(user_name = user_name, email = email, password = password)

    return new_user



# insert the new log data into the database
def insert_new_log(user_id, first_name_dated, last_name_dated, date_of_the_date, city_met, overall_rating, app_met, key_takeaway, description, contact_info, picture, sharing):
    """Insert the log data into the log database"""

    new_log = Log(user_id = user_id, 
                first_name_dated = first_name_dated, 
                last_name_dated = last_name_dated, 
                date_of_the_date =date_of_the_date, 
                city_met= city_met,
                overall_rating = overall_rating, 
                app_met= app_met,
                key_takeaway = key_takeaway,
                description = description,
                contact_info= contact_info,
                picture = picture,
                sharing = sharing)

    return new_log



# get the log data from the logs datatable --> store in list of objects
def get_user_logs_by_user_id(user_id):
    """get the logs created by the user_id and store in log"""

    logs_under_id = Log.query.filter_by(user_id=user_id).all()

    return logs_under_id 


# insert the new friend data into the database
def insert_new_friend(user_email, friend_email, friend_username):
    """Insert the friend data into the friend database"""

    new_friend = Friend(user_email = user_email, friend_email = friend_email, friend_username = friend_username)

    return new_friend

# insert the new comment data into the database
def insert_new_comment(user_email, log_id, comment):
    """Insert the comment data into the comment database"""

    new_comment = Comment(commentor_email = user_email, log_id = log_id, comments = comment)

    return new_comment


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    