from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

class Name(db.Model):
    __tablename__ = 'names'

    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'
        