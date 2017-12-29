# webform/views.py

# IMPORTS
import os
import shutil
from flask import render_template, request, redirect, url_for, flash
from webform import app
from .forms import CodeForm

# ROUTES
@app.route('/', methods=['GET', 'POST'])
def webform():
    form = CodeForm(request.form)
    show_link = False
    if request.method == 'POST':
        with open('webform/templates/new_template.html', 'w') as template_file:
            template_file.write(form.data['html'])
        with open('webform/templates/new_template.html', 'r') as read_file:
            for i in read_file:
                print(i)
        show_link = True
    """Render code form"""
    return render_template('webform.html', form=form, show_link=show_link)

@app.route('/jinja', methods=['GET'])
def jinja():
    return render_template('new_template.html')