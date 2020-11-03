from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import User,Subscribe

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
    name = StringField('Confirm username', validators=[Required()])
    email = StringField('Your Email Address', validators=[Required(), Email()])
    submit = SubmitField('Subscribe')


    def validate_email(self, email):
        email = Subscribe.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('This email is already subscribed.')

