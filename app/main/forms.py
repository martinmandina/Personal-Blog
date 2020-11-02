from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class BlogForm(FlaskForm):
    category=TextAreaField('Input your Blog', validators = [Required()])
    title = TextAreaField('Input Your name',validators = [Required()])
    content = TextAreaField('blog',validators = [Required()])
    submit = SubmitField('Submit')