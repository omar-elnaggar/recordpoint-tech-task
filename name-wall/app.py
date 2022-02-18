from flask import Flask, redirect, url_for, render_template, request, flash
import psycopg2
from models import db, Name


app = Flask(__name__)
app.secret_key = "something_secret"
app.config['SQLALCHEMY_DATABASE_URI'] =  'postgresql://postgres:postgres@postgres/names'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        new_name = Name(name=request.form['nm'])
        db.session.add(new_name)
        db.session.commit()
        flash(f'Thank you for signing your name {new_name.name}!', 'success')
        return render_template('index.html', values=show_names())
    else:
        return render_template('index.html', values=show_names())

def show_names():
    if db.engine.has_table('names'):
        return db.session.query(Name).all()

if __name__ == '__main__':
    app.run(debug=True)
