from system.db import db


class User(db.Model):
    telegram_id = db.Column(db.Integer, primary_key=True)
    simple_mode = db.Column(db.Boolean)

    def __repr__(self):
        return '<User {}>'.format(self.telegram_id)
