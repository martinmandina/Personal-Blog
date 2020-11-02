from flask import render_template,request,redirect,url_for
from . import main
from .forms import BlogForm
from .. import db
from ..models import User,BlogPost,Comment,Subscribe
from flask_login import login_required
from ..auth.forms import SubscriptionForm



@main.route('/', methods =  ["GET","POST"])
def index():
    sub_form = SubscriptionForm()
    blog = BlogPost.query.all()

    title = 'Home - Personal Blogging Website'
    return render_template('index.html',blog = blog,sub_form = sub_form,title = title)

@main.route('/blog/newblog', methods=['GET', 'POST'])
@login_required
def blog_new():
    form = BlogForm()
    if form.validate_on_submit():
        newblog = BlogPost(category = form.category.data,content = form.newblog.data)
        db.session.add(blog)
        db.session.commit()

    return redirect(url_for('main.index'))
    return render_template('blognew.html',form=form,blog=blog)




