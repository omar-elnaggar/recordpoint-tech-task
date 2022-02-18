from flask import Flask, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "something_secret"

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        name = request.form['nm']
        flash(f'Thank you for signing your name {name}!', 'success')
        return render_template('index.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
