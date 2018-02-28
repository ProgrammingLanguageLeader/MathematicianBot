from flask_sqlalchemy import SQLAlchemy

from math_bot.conversation_states import ConversationStates


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
    mode = db.Column(
        db.Enum(ConversationStates),
        nullable=False
    )

    def __repr__(self):
        return '<User {}>'.format(self.telegram_id)
