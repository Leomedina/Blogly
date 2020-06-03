from models import User, db
from app import app

#Create all tables
db.drop_all()
db.create_all()

#If it isn't empty the table
User.query.delete()

Leo = User(first_name="Leo", last_name="Medina")
Danny_DeVito = User(first_name="Danny", last_name="DeVito", img_url="https://media.phillyvoice.com/media/images/Screen_Shot_2018-11-17_at_7.46.2e16d0ba.fill-1200x630-c0.png")
Danny_Trejo = User(first_name="Danny", last_name="Trejo", img_url="https://media.npr.org/assets/img/2014/08/01/ap100825058736-f7dc5ba8d85f12c98b7cdcec463d553766306b81-s1600-c85.jpg")
Trevor_Noah = User(first_name="Trevor", last_name="Noah", img_url="https://a9p9n2x2.stackpathcdn.com/wp-content/blogs.dir/1/files/2020/05/trevor-noah-facebook-black-enterprise.jpg")

#Adding new Users into the session
db.session.add(Leo)
db.session.add(Danny_DeVito)
db.session.add(Danny_Trejo)
db.session.add(Trevor_Noah)

#Commits the session and saves it to the server
db.session.commit()