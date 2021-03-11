from datetime import datetime

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# Handles with pythonpath ModuleNotFoundError
import sys

sys.path = ['', '..'] + sys.path[1:]

from api import create_app, create_db

app = create_app()
db = create_db(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Text)
    geo = db.Column(db.String(30), nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Address %r>' % self.zipcode


if __name__ == '__main__':
    manager.run()
