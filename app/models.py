from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager

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

    blogs = db.relationship('Blog',backref='author',lazy='dynamic')


    # securing passwords
    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key=True)
    blog_title = db.Column(db.String(255), nullable = False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(15), nullable=False, default='MartinJohn')

    user_id = db.Column(db.Integer,db.ForeignKey ('users.id'),nullable=False)
    comment = db.relationship('comments', backref='blog', lazy='dynamic')

    def __repr__(self):
        return f'Title {self.Blog_title}'

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
        return f'User:{self.username}'





   