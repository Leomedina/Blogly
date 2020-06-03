from models import *

class Utilities:
    @classmethod
    def add_user(cls, first_name, last_name, img_url):
        new_user = User(first_name=first_name, last_name=last_name, img_url=img_url)
        db.session.add(new_user)
        db.session.commit()
        return new_user.id

    @classmethod
    def delete_user(cls, user_id):
        User.query.filter_by(id=user_id).delete()
        db.session.commit()
        return True