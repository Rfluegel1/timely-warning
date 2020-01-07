
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, Form, FloatField, BooleanField, StringField, PasswordField, validators
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from config import Config

csrf = CSRFProtect()
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///timely_warning.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf.init_app(app)

from models import Reports
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

class WordForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired()]);
    lat = FloatField("Latitude", [validators.NumberRange(min=43, max=45, message="Latitude value not in range 43 to 45"), validators.DataRequired()])
    lon = FloatField("Longitude", [validators.NumberRange(min=-94, max=-92, message="Longitude value not in range -92 to -94"), validators.DataRequired()])
    description = StringField("Description")
    submit = SubmitField("Submit")

@app.route('/')
def home():
    form = WordForm()
    return render_template('home.html', form=form)
    #return'Choose: submit report or view reports'

@app.route('/submit')
def submit():
    form = WordForm()
    return render_template('submit.html', form=form)
    #return 'Submit your report here'

@app.route('/view')
def view():
    form = WordForm()
    reports = Reports.query.all()
    print(reports)
    return render_template('view.html', form=form, list=reports)
    #return 'View all reports here'

@app.route('/insert', methods=['POST','GET'])
def insert():
    form = WordForm()
    if form.validate_on_submit():
        name = form.name.data
        lat = form.lat.data
        lon = form.lon.data
        desc = form.description.data
    else:
        return render_template('submit.html', form=form)
    print(name)
    print(lat)
    print(lon)
    print(desc)
    # Nuke database
    # db.session.execute('DELETE FROM reports WHERE true')
    rows = db.session.execute('SELECT * FROM reports')
    id = len(rows.fetchall()) + 1
    print(id)
    #insert = 'INSERT INTO reports (id, name, lon, lat, description) VALUE ({}, \'{}\', \'{}\', \'{}\', \'{}\')'.format(id, name, lat, lon, desc)
    #print(insert)
    r = Reports(id, name, lat, lon, desc)
    db.session.add(r)
    db.session.commit()
    return render_template('successful.html')

if __name__ == '__main__':
    app.run(debug=True, port=8003, host="0.0.0.0")
