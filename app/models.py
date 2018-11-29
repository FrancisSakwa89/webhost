from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index =True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(5000))
    profile_pic_path = db.Column(db.String)
    pass_secure = db.Column(db.String(255))
    date_joined = db.Column(db.DateTime,default=datetime.utcnow)

    post = db.relationship('post',backref = 'user',lazy = "dynamic")

    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer,primary_key = True)
    post_title = db.Column(db.String)
    post_content = db.Column(db.String(1000))
    category = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)

    comments = db.relationship('Comment',backref =  'post_id',lazy = "dynamic")

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_post(cls,category):
        post = post.query.filter_by(category=category).all()
        print(post)
        return post

    @classmethod
    def get_post(cls,id):
        post = post.query.filter_by(id=id).first()

        return post

    @classmethod
    def count_posts(cls,uname):
        user = User.query.filter_by(username=uname).first()
        post = post.query.filter_by(user_id=user.id).all()

        post_count = 0
        for post in post:
            post_count += 1

        return post_count

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(1000))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    post = db.Column(db.Integer,db.ForeignKey("post.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,post):
        comments = Comment.query.filter_by(post_id=post).all()
        return comments
