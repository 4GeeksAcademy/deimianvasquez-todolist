from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    todos = db.relationship("Todo", uselist=True, backref='user')


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
        }