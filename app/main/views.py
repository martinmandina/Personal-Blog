from flask import render_template,request,redirect,url_for
from . import main
import os
from .forms import BlogForm,NewAccountForm,CommentForm
from .. import db,photos
from ..models import User,BlogPost,Comment,Subscribe
from flask_login import login_required,current_user
from app.auth.forms import SubscriptionForm



@main.route('/', methods =  ["GET","POST"])
def index():
    form = BlogForm()

    blogs = BlogPost.query.all()
    title = 'Home - Personal Blogging Website'
    form = SubscriptionForm()
    if form.validate_on_submit():
        post = BlogPost(title=form.title.data, content=form.content.data)
        email = Subscribe(email=form.email.data)
        db.session.add(email)
        db.session.commit()
   
    return render_template('index.html', title=title,form=form,blogs=blogs)
    


@main.route("/blog/new", methods=['GET', 'POST'])
@login_required
def new_post():
    if current_user.username != 'JohnJohn':
    
        form = BlogForm()
    if form.validate_on_submit():
        post = BlogPost(title=form.title.data, content=form.Blog_content.data)
        db.session.add(post)
        db.session.commit()
       
        return redirect(url_for('main.index'))
    return render_template('new_blog.html', title='New Post', form=form, New='New Post')

@main.route('/blog/mine', methods=['GET', 'POST'])
def mine():
    form = BlogForm()

    if form.validate_on_submit():
        title = form.title.data
        Blog_post = form.Blog_post.data

        blog = BlogPost(blog_name=title, blog_info=Blog_post)

        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('.blogpost'))
    posts = BlogPost.query.order_by(BlogPost.time_post.desc()).all()
    
    return render_template('my_blog.html', form=form, posts=posts)


@main.route('/blog/about')
def about():
    title = 'Blog Description'

    return render_template('description.html', title=title)


@main.route("/user", methods=['GET', 'POST'])
@login_required
def profile():
    form = NewAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            # picture_file = load_picture(form.picture.data)
            current_user.username = form.username.data
            current_user.email = form.email.data
            db.session.commit()
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile/' + current_user.image_file)
    return render_template('profile/profile.html', title='Account', image_file=image_file, form=form)

@main.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comments(comment=comment, post_id=post_id, user=current_user)
        new_comment.save_comments()
        return redirect(url_for('main.post', post_id=post.id))
    comments = Comments.query.filter_by(post_id=post_id).all()
    return render_template('post.html', title=post.title, post=post, comment_form=form, comments=comments)

