from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

requiredField = InputRequired(message="*required")

class AddPetForm(FlaskForm):
    """Blueprint for rendering the add pet or edit pet form."""
    
    name = StringField("Name", validators=[requiredField])
    species = StringField("Species", validators=[requiredField, AnyOf(values=['dog', 'cat', 'porcupine'])])
    photo_url = StringField('Photo URL', validators=[Optional(), URL(message='Link must be in URL format.')])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30.")])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available?", default='checked')
