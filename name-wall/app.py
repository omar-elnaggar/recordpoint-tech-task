from flask import Flask, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, Name

app = Flask(__name__)
app.secret_key = "something_secret"
app.config['SQLALCHEMY_DATABASE_URI'] =  'postgresql://pguser:pgpass@postgres/names'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        new_name = Name(name=request.form['nm'])
        db.session.add(new_name)
        db.session.commit()
        flash(f'Thank you for signing your name {new_name.name}!', 'success')
        return render_template('index.html')
    else:
        return render_template('index.html')

    
def get_names():
    return db.session.query.all()

if __name__ == '__main__':
    app.run(debug=True)
