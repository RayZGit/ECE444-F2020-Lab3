from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import Flask, render_template
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('/activity1/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('/activity1/500.html'), 500

@app.route('/')
def index():
    return render_template('/activity1/base.html')

@app.route('/user/<name>')
def user(name):
    return render_template('/activity1/user.html', name = name, current_time=datetime.utcnow())


if __name__ == "__main__":
    app.run(debug=True)