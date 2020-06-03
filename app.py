from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "SecretKeys"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def show_users():
    """Show a list of all users"""
    users = User.query.all()
    return render_template("home.html", users = users)

@app.route("/users")
def display_all_users():
    """Show a list of all users"""
    users = User.query.all()
    return render_template("users.html", users = users)

@app.route("/users/new")
def new_user_page():
    """Show a page with a new user form"""
    return render_template("form.html")

@app.route("/users/new", methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    img_url = request.form["url"]

    new_user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect(f"/users/{new_user.id}")

@app.route("/users/<int:user_id>")
def show_user_page(user_id):
    """Show User Details"""
    user = User.query.get_or_404(user_id)
    return render_template("profile.html", user=user)
