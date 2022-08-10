"""Server for dating log app."""

from crypt import methods
import email
from flask import (Flask, jsonify, render_template, request, flash, session, redirect)
from model import connect_to_db, db, User, Log
import crud
import cloudinary.uploader
import os
from operator import itemgetter, attrgetter

from jinja2 import StrictUndefined

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


CLOUDINARY_KEY = os.environ["CLOUDINARY_KEY"]
CLOUDINARY_SECRET = os.environ["CLOUDINARY_SECRET"]
CLOUD_NAME = "dkmt3jwtx"


@app.route("/")
def homepage():
    """homepage"""

    return render_template("homepage.html")


@app.route("/user", methods = ["POST"])
def create_new_user():
    """create new user in the database and show message if the email or user_name were registered"""

    email = request.form.get("email")
    user_name = request.form.get("user_name")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    # existing user name in a list
    existing_user_names = []
    for n in User.query.all():
        existing_user_names.append(n.user_name)

    print(existing_user_names)

    if user:
        flash("Cannot create an account with that email. Try again.")

        return redirect("/")
    elif user_name in existing_user_names:
        flash("Username taken. Try again.")

        return redirect("/")
    else:
        new_user = crud.insert_new_user(user_name, email, password)
        
        db.session.add(new_user)
        db.session.commit()
        
        session["user_email"] = new_user.email

        flash(f"Account created! Welcome {new_user.user_name}.")

        return redirect(f"/user/{new_user.email}")



@app.route("/login", methods = ["POST"])
def process_login():
    """manage the log in process"""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("The email or password you entered was incorrect. Please try again.")

        return redirect("/")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        
        flash(f'Welcome back, {user.user_name}!')

        return redirect(f"/user/{user.email}")


@app.route("/user/<user_email>")
def show_user_logs(user_email):
    """show individual user page with the library of each log"""
    
    user = crud.get_user_by_email(user_email)

    list_of_log_objects = crud.get_user_logs_by_user_id(user.user_id)

    return render_template("user_details.html", user = user, list_of_log_objects = list_of_log_objects)

# api here
@app.route("/user/sorting/<user_email>/api", methods = ["POST"] )
def get_user_logs_in_api(user_email):
    """fetch the sorting info and pass it throgh api so that sort.jsx can take it"""

    # sorting_object = request.json.get("sorting_object")
    # sorting_rule = request.json.get("sorting_rule")

    user = crud.get_user_by_email(user_email)
    list_of_log_objects = crud.get_user_logs_by_user_id(user.user_id)

    # sorting scenario
    if sorting_rule == "High_to_low":
        sorted_list_objects = sorted(list_of_log_objects, key=attrgetter(sorting_object), reverse= True)
    elif sorting_rule == "Low_to_high":
        sorted_list_objects = sorted(list_of_log_objects, key=attrgetter(sorting_object), reverse= False)
        
    logs_dictionary = {}

    for list_obj in sorted_list_objects:
        logs_dictionary[list_obj.log_id] = {}
        logs_dictionary[list_obj.log_id]["name"] = list_obj.first_name_dated + " "+ list_obj.last_name_dated
        logs_dictionary[list_obj.log_id]["overall_rating"] = list_obj.overall_rating
        logs_dictionary[list_obj.log_id]["picture"] = list_obj.picture

    return jsonify(logs_dictionary)


@app.route("/new_dating_log")
def create_new_dating_log():
    """create a template for the users to key in the dating info"""

    return render_template("new_dating_log.html")


@app.route("/date_info", methods = ["POST"])
def log_date_info():
    """log the dating info data in the db"""

    user_id = crud.get_user_by_email(session.get("user_email")).user_id
    user_email = session.get("user_email")
    first_name_dated = request.form.get("first_name_dated")
    last_name_dated = request.form.get("last_name_dated")
    date_of_the_date = request.form.get("date_of_the_date")
    city_met= request.form.get("city_met")
    overall_rating = request.form.get("overall_rating")
    app_met= request.form.get("app_met")
    key_takeaway = request.form.get("key_takeaway")
    description = request.form.get("description")
    contact_info = request.form.get("contact_info")
    picture_from_post = request.files["picture"]

    dictionary_picture_result = cloudinary.uploader.upload(
        picture_from_post, 
        api_key = CLOUDINARY_KEY,
        api_secret = CLOUDINARY_SECRET,
        cloud_name = CLOUD_NAME)

    picture = dictionary_picture_result["secure_url"]
   
    new_log = crud.insert_new_log(user_id, first_name_dated, last_name_dated, date_of_the_date, city_met, overall_rating, app_met, key_takeaway, description, contact_info, picture)
    
    db.session.add(new_log)
    db.session.commit()

    return redirect(f'/user/{user_email}')

 

@app.route("/user/logs/<log_id>")
def show_log_detail(log_id):
    """show the created log details"""

    log_object = Log.query.filter_by(log_id=log_id).first()

    return render_template("created_log_detail_page.html", log_object = log_object)


@app.route("/user/logs/delete/<log_id>")
def delete_current_log(log_id):
    """delete the log in the log datatable"""

    delete_log = Log.query.filter(Log.log_id == log_id).first()
    db.session.delete(delete_log)
    db.session.commit()

    user_email = session["user_email"]
    
    return redirect(f'/user/{user_email}')


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
