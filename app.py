from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import *
from utilities import *

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

# USER ROUTES #
@app.route("/users")
def display_all_users():
    """Show a list of all users"""
    users = User.query.all()
    return render_template("users.html", users = users)

@app.route("/users/new")
def new_user_page():
    """Show a page with a new user form"""
    return render_template("form.html")

@app.route("/users/<int:user_id>")
def show_user_page(user_id):
    """Show User Details"""
    user = User.query.get_or_404(user_id)
    posts = user.posts
    return render_template("profile.html", user=user, full_name=user.get_full_name(), posts=posts)

@app.route("/users/<int:user_id>/edit")
def edit_form(user_id):
    """Delete User"""
    user = User.query.get_or_404(user_id)
    return render_template("edit.html", user = user, full_name = user.get_full_name())

# USER CONTENT ROUTES
@app.route("/posts/<int:post_id>")
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    user = post.author_info
    return render_template("post.html", user = user, full_name = user.get_full_name(), post = post)

@app.route("/users/<int:user_id>/posts/new")
def new_post_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('post-form.html', user = user, full_name = user.get_full_name())

@app.route("/users/<int:user_id>/posts")
def reroute(user_id):
    return redirect(f'/users/{user_id}')

# POST ROUTES #
@app.route("/users/new", methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    img_url = request.form["url"]

    new_user_id = Utilities.add_user(first_name, last_name, img_url)
    return redirect(f"/users/{new_user_id}")

@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    """Delete User"""
    Utilities.delete_user(user_id)
    return redirect("/users")

@app.route("/users/<int:user_id>/edit", methods=["POST"])
def edit_user(user_id):
    """Edit User"""
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    img_url = request.form["img_url"]

    Utilities.edit_user(user_id, first_name, last_name, img_url)
    return redirect(f"/users/{user_id}")

@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def add_new_post(user_id):
    title = request.form["title"]
    content = request.form["content"]
    Utilities.new_post(user_id, title, content)
    return redirect(f"/users/{user_id}")

@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    """Delete Post"""
    Utilities.delete_post(post_id)
    return redirect("/")