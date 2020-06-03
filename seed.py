from models import User, db, Post
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

leo_post1= Post(title="Test Post", content="Loren Ipsum is placeholder text originally written in latin", author=1)
Dt_Post1 = Post(title="Chest Tattoo", content="The tattoo on his chest of a woman wearing a sombrero (you see it in almost all of his movies).", author=3)
Dt_Post2 = Post(title="Heat 1995", content="His character's name in Heat (1995) was Trejo.", author=3)
Dt_Post3 = Post(title="Hollywood", content="He and director Robert Rodriguez are second cousins.", author=3)
Tn_Post1 = Post(title="The Daily", content="Right Now all daily shows are filmed at home", author=4)
Dd_Post1 = Post(title="The GOAT", content="Danny DeVito is in fact the GOAT", author=2)

#Adding and commiting new Users into the session
db.session.add(Leo)
db.session.add(Danny_DeVito)
db.session.add(Danny_Trejo)
db.session.add(Trevor_Noah)
db.session.commit()


#Adding and commiting new post to the session
db.session.add(leo_post1)
db.session.add(Dt_Post1)
db.session.add(Dt_Post2)
db.session.add(Dt_Post3)
db.session.add(Tn_Post1)
db.session.add(Dd_Post1)
db.session.commit()

