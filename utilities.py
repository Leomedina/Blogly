from models import *

class Utilities:
    """UTILITIES FOR APP.PY"""
    #
    # ADD UTILITIES
    #
    @classmethod
    def add_user(cls, first_name, last_name, img_url):
        new_user = User(first_name=first_name, last_name=last_name, img_url=img_url)
        db.session.add(new_user)
        db.session.commit()
        return new_user.id

    @classmethod
    def add_tag(cls, name):
        new_tag = Tag(name=name)
        db.session.add(new_tag)
        db.session.commit()
        return new_tag.id

    @classmethod
    def new_post(cls, user_id, title, content):
        post = Post(title=title, content=content, author=user_id)
        db.session.add(post)
        db.session.commit()
        return True

    #
    #DELETE UTILITIES
    #

    @classmethod
    def delete(cls, id, table):
        item = db.session.query(table).filter(table.id==id).first()
        db.session.delete(item)
        db.session.commit()
        return True

    #
    # EDIT UTILITIES
    #
    @classmethod
    def edit_user(cls, user_id, first_name='', last_name="", img_url=""):
        user = User.query.get(user_id)
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if img_url:
            user.img_url = img_url
        db.session.add(user)
        db.session.commit()
        return True

    @classmethod
    def edit_post(cls, post_id, title="", content=""):
        post = Post.query.get_or_404(post_id)
        if title:
            post.title = title
        if content:
            post.content = content
        db.session.add(post)
        db.session.commit()
        return True

    @classmethod
    def edit_tag(cls, tag_id, name):
        tag = Tag.query.get_or_404(tag_id)
        tag.name = name
        db.session.add(tag)
        db.session.commit()
        return True