from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError



class NewAccountForm(FlaskForm):
    username = StringField('Your Username', validators=[Required()])
    email = StringField('Input Email Address', validators=[Email()])
    picture = FileField('Update Profile Picture', validators=[Required()])
    submit = SubmitField('Update Information')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is already taken.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is already taken.')


class BlogForm(FlaskForm):
    title = TextAreaField('Choose your blog name',validators = [Required()])
    category=TextAreaField('Post your Blog', validators = [Required()])
    Blog_content = TextAreaField('blog content')
    submit = SubmitField('Submit')

