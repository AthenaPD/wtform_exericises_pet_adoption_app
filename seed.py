"""Seed file to make sample pets for database."""

from models import Pet, db
from app import app


with app.app_context():
    # Create all tables
    db.drop_all()
    db.create_all()

    # Empty table if it's not
    Pet.query.delete()

    # Add some pets
    sophie = Pet(name='Sophie', species='dog', age=4, notes='Mini Aussie', available=True)
    lady = Pet(name='Lady Grace', species='porcupine', age=1, available=True)
    handsome = Pet(name='Handsome', species='porcupine', available=True)
    boba = Pet(name='Boba', species="cat", notes='black mixed breed', available=True)
    creamy = Pet(name='Creamy', species='cat', age=3, notes='white mixed breed', available=False)

    db.session.add_all([sophie, lady, handsome, boba, creamy])
    db.session.commit()
