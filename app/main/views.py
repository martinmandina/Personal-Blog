from flask import render_template,request,redirect,url_for
from . import main
from .forms import BlogForm
from .. import db
from ..models import User,BlogPost,Comment,Subscribe
from flask_login import login_required



@main.route('/', methods =  ["GET","POST"])
def index():
    form = BlogForm()

    if form.validate_on_submit():
        title = form.title.data
        Blog_content = form.Blog_content.data

        blog = Blog(blog_name=title, blog_info=Blog_post)
        db.session.add(blog)
        db.session.commit()
      
        return redirect(url_for('.blogpost'))
    posts = BlogPost.query.order_by(BlogPost.time_post.desc()).all()
    
    return render_template('index.html',form=form, posts=posts)


    

    title = 'Home - Personal Blogging Website'
    return render_template('index.html', title = title)

@main.route('/blognew/', methods=['GET', 'POST'])
def blog_new():
    form = BlogForm()
    subscribe = Subscribe.query.all()
    if form.validate_on_submit():
        title = form.title.data
        Blog_content = form.Blog_content.data

        blog = Blog(blog_name=title, blog_info=Blog_post)

        db.session.add(blog)
        db.session.commit()

    return redirect(url_for('.index'))
    posts = Blog.query.order_by(Blog.date_posted.desc()).all()
    return render_template('blognew.html', form=form, posts=posts)


