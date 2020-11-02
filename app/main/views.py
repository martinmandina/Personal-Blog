from flask import render_template,request,redirect,url_for
from . import main
from .forms import BlogForm,NewAccountForm
from .. import db
from ..models import User,BlogPost,Comment,Subscribe
from flask_login import login_required
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


@main.route("/user", methods=['GET', 'POST'])
@login_required
def profile():
    form = NewAccountForm()
    if form.validate_on_submit():
        
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('profile/profile.html', title='Account',form=form)

