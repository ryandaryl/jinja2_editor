# webform/views.py

# IMPORTS
import os
import shutil
import json
from flask import render_template, request, redirect, url_for, flash
from webform import app
from .forms import CodeForm

def new_template(html):
    with open('webform/templates/new_template.html', 'w') as template_file:
        template_file.write(html)
    with open('webform/templates/new_template.html', 'r') as read_file:
        for i in read_file:
            print(i)

# ROUTES
@app.route('/', methods=['GET', 'POST'])
def webform():
    form = CodeForm(request.form)
    show_link = False
    if request.method == 'POST':
        new_template(form.data['html'])
        data = json.loads(form.data['pythonobj']) if form.data['pythonobj'] else []
        return render_template('new_template.html', data=data)
    """Render the form"""
    return render_template('webform.html', form=form, show_link=show_link)