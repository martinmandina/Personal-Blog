from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('an account with this email has been registered')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('The username is already taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')            
    
class SubscriptionForm(FlaskForm):
    name = StringField('Enter your username', validators=[Required()])
    user_email = StringField('Your Email Address', validators=[Required(), Email()])
    submit = SubmitField('Subscribe')

def validate_name(self, data_field):
    if User.query.filter_by(username=data_field.data).first():
        raise ValidationError('That username is already taken')

def validate_user_email(self, data_field):
    if User.query.filter_by(email=data_field.data).first():
        raise ValidationError('There is an account with that email')

        
