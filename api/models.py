from datetime import datetime
from manager import db


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Text)
    geo = db.Column(db.String(30), nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Address %r>' % self.zipcode

