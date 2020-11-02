from flask import render_template,request,redirect,url_for
from . import main
from manage import app
import secrets
import os
from .forms import BlogForm,NewAccountForm
from .. import db
from ..models import User,BlogPost,Comment,Subscribe
from flask_login import login_required,current_user
from app.auth.forms import SubscriptionForm



@main.route('/', methods =  ["GET","POST"])
def index():
    form = BlogForm()

    title = 'Home - Personal Blogging Website'
    
    form = SubscriptionForm()
    if form.validate_on_submit():
        email = Subscribe(email=form.email.data)
        db.session.add(email)
        db.session.commit()
    return render_template('index.html', title=title, form=form)
    


@main.route("/blog/new", methods=['GET', 'POST'])
@login_required
def new_post():
    if current_user.username != 'JohnJohn':
        abort(404)

    form = BlogForm()

    if form.validate_on_submit():
        post = BlogPost(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
       
        return redirect(url_for('main.index'))
    return render_template('new_blog.html', title='New Post', form=form, New='New Post')

@main.route('/blog/about')
def about():
    title = 'Blog Description'

    return render_template('description.html', title=title)


def load_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _,pic= os.path.splitext(form_picture.filename)
    picture_fn = random_hex + pic
    picture_path = os.path.join(app.root_path, 'static/profile/', picture_fn)
    form_picture.save(picture_path)
    current_user.image_file = picture_fn
    image_file = url_for('static', filename='profile/' + current_user.image_file)


@main.route("/user", methods=['GET', 'POST'])
@login_required
def profile():
    form = NewAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = load_picture(form.picture.data)

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile/' + current_user.image_file)
    return render_template('profile/profile.html', title='Account', image_file=image_file, form=form)
