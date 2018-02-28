from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    telegram_id = db.Column(
        db.Integer,
        index=True,
        unique=True,
        nullable=False
    )
    simple_mode = db.Column(
        db.Boolean
    )

    def __repr__(self):
        return '<User {}>'.format(self.telegram_id)
