from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
             "id": self.id,
             "email": self.email,
             # do not serialize the password, its a security breach
         }

class Todo(db.Model):
    __tablename__="todo"
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(80), nullable=False, unique=True)
    done = db.Column(db.Boolean(), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeingKey("user.id"))

    def serialize(self):
        return{
            "id": self.id,
            "label": self.label,
            "done": self.done,
            "user_id": self.user_id
        }

