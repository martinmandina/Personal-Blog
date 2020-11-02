from flask import render_template,request,redirect,url_for
from . import main



@main.route('/', methods =  ["POST","GET"])
def index():

    

    title = 'Home - Personal Blogging Website'
    return render_template('index.html', title = title)

