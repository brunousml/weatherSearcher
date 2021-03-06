from app.app import db
from datetime import datetime


class Address(db.Model):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Text)
    zipcode = db.Column(db.String(10), nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    updated = db.Column(db.Datatime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<id {}>'.format(self.id)