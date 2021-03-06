
from datetime import datetime

from app.app import db


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Text)
    zipcode = db.Column(db.String(10), nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    updated = db.Column(db.Datatime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Address %r>' % self.zipcode


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Text)
    zipcode = db.Column(db.String(10), nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    fingerprint = db.Column(db.Text)
    created_at = db.Column(db.Datatime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Log %r>' % self.zipcode