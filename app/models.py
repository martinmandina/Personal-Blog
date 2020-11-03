from . import db,login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


@login_manager.user_loader
def load_user(user_id):

    """
    @login_manager.user_loader Passes in a user_id to this function
    Function queries the database and gets a user's id as a response
    """
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(5000))
    profile_pic_path = db.Column(db.String(255))
    password_secure = db.Column(db.String(5000))
    image_file = db.Column(db.String(70), nullable=False, default='default.jpg')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    blogs = db.relationship('BlogPost',backref='user',lazy='dynamic')


    # securing passwords
    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'

class BlogPost(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key=True)

    title = db.Column(db.String(255), nullable = False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(15), nullable=False, default='MartinJohn')
    time_post = db.Column(db.Time, default=datetime.utcnow())
    category= db.Column(db.String(),index = True)

    user_id = db.Column(db.Integer,db.ForeignKey ('users.id'))
    comments = db.relationship('Comment', backref='blog', lazy='dynamic')

    def __repr__(self):
        return f'User {self.title}'

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    comment = db.Column(db.String(5000))

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))

    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Comment:comment{self.comment}'

class Subscribe(UserMixin, db.Model):
    __tablename__="subscribes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    title = db.Column(db.String(255))
    email = db.Column(db.String(100), unique=True)


    def save_subscribes(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_subscribes(cls,id):
        return Subscribe.query.all()
         

    def __repr__(self):
        return f'User {self.email}'       







   