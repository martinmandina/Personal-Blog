from flask import render_template,request,redirect,url_for
from . import main
from .. import db
from ..models import User
from flask_login import login_required



@main.route('/', methods =  ["POST","GET"])
def index():
    form = BlogForm()
    

    

    title = 'Home - Personal Blogging Website'
    return render_template('index.html', title = title)

