from flask import render_template,redirect,url_for
from ..models import User
from .forms import RegistrationForm
from .. import db
from . import auth

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        
        db.session.add(user)
        db.session.commit()

        flash('Register here')
        return redirect(url_for('auth.login'))
        title = "Blog: Create New Account"
    return render_template('auth/register.html',registration_form = form)
