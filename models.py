"""Setup models for the pet adoption app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    photo_url = db.Column(db.Text, default="https://i.etsystatic.com/41317592/r/il/85faff/5325346794/il_1588xN.5325346794_1fms.jpg")
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"<Pet {self.name} {self.species}>"
