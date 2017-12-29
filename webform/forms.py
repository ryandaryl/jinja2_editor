from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, StringField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class CodeForm(FlaskForm):
    html = TextAreaField(
              'Enter some Jinja2 and HTML here:',
              default='{% for i in data %}\nline {{ i }}<br>\n{% endfor %}'
    )
    pythonobj = TextAreaField(
              'Paste JSON here:',
              default='[1,2,3]'
    )