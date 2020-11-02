from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class BlogForm(FlaskForm):
    title = TextAreaField('Your Preffered blog name',validators = [Required()])
    category=TextAreaField('Post your Blog', validators = [Required()])
    Blog_content = TextAreaField('blog content')
    submit = SubmitField('Submit')
