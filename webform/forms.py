from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, StringField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class CodeForm(FlaskForm):
    html = TextAreaField('Enter some Jinja2 and HTML here:')
    pythonobj = TextAreaField('Paste a Python object here:')