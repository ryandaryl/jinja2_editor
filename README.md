
# Compile Jinja2 to HTML with this Python/Flask application
This is an app for trying out the [Jinja2](http://jinja.pocoo.org) templating language.
## How to use it
- Put some Jinja2 into the box.
- Enter some data.
	- Data is optional. 
	- Use JSON format
	- Data will be available as "data"
- Press submit.

<img src="https://image.ibb.co/h1nTZG/jinja2_editor1.png" alt="Jinja2 editor" border="0" width="40%" /><img src="https://image.ibb.co/ebrBob/jinja2_editor2.png" alt="Jinja2 editor" border="0" width="40%" hspace=80/>
You'll get some nice, compiled HTML.

## How it works
The user enters Jinja2 into the form, and the script is compiled into HTML and returned to the browser. Any number of objects, arrays and environment variables can be added as JSON, and used by the Jinja2 template.

See it working [here](https://jinja-rdm.herokuapp.com).

The application itself is built with Jinja2 as the templating system, and simply writes user code as a new Jinja2 template. The script is compiled like any other Jinja2 template. You can look at [views.py](https://github.com/ryandaryl/jinja2_editor/blob/master/webform/views.py) to see how it works, or...

## Deploy to Heroku
By clicking the button below.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
