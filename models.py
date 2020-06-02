from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True)
    first_name = db.Column(db.String(15), nullable = False)
    last_name = db.Column(db.String(15), nullable = False)
    img_url = db.Column(db.String(150), nullable= False, default = 'https://i.imgur.com/SczclW9.jpg')

    def __repr__(self):
        return f"<UserId: {self.id} Name: {self.first_name} Last Name: {self.last_name} Profile Pic: {self.img_url}"