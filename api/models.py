# from api import db
# import datetime
#
#
# class AddressModel(db.Model):
#     __tablename__ = 'addresses'
#
#     id = db.Column(db.Integer, primary_key=True)
#     address = db.Column(db.Text)
#     zipcode = db.Column(db.String(10), nullable=False)  # todo: use json data
#     temperature = db.Column(db.Integer, nullable=False)  # todo: use json data
#     updated = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
#
#     def __repr__(self):
#         return '<id {}>'.format(self.id)
