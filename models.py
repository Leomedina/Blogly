from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User Model"""

    __tablename__ = "users"
    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True)
    first_name = db.Column(db.String(15), nullable = False)
    last_name = db.Column(db.String(15), nullable = False)
    img_url = db.Column(db.String(600), nullable= False, default = "https://st2.depositphotos.com/1009634/7235/v/450/depositphotos_72350117-stock-illustration-no-user-profile-picture-hand.jpg")
    posts = db.relationship("Post", backref="author_info", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<UserId: {self.id} Name: {self.first_name} Last Name: {self.last_name} Profile Pic: {self.img_url}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    """Post Model"""

    __tablename__ = "posts"
    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True)
    title = db.Column(db.String(20),
                         nullable = False)
    content = db.Column(db.String(500),
                        nullable = False)
    created_at = db.Column(db.DateTime(timezone=True), 
                        default=func.now())
    author = db.Column(db.Integer,
                        db.ForeignKey('users.id'), nullable = False)
    post_tags = db.relationship("Post_Tag", backref="post_info", cascade="all, delete-orphan")

    def __repr__(self):
        author_info = f"PostId: {self.id} Author: {self.author_info.get_full_name()}"
        post_info = f"Created At: {self.created_at} Content= {self.content}"
        return f"<{author_info} {post_info}>"

class Tag(db.Model):
    """Tag Model"""

    __tablename__ = "tags"
    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True)
    name = db.Column(db.Text, nullable = False)

    post_tags = db.relationship("Post_Tag", backref = "tag_info", cascade="all, delete-orphan")

class Post_Tag(db.Model):
    """Many-To-Many Tag/Post Model"""

    __tablename__ = "post_tags"
    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True)
    tag_id = db.Column(db.Integer,
                        db.ForeignKey('tags.id'))
    post_id = db.Column(db.Integer,
                        db.ForeignKey('posts.id'))