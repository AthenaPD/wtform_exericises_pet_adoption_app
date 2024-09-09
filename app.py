from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from form import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoptable_pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_all_pets():
    """Render home page to list all pets."""
    adoptable_pets = Pet.query.filter_by(available=True).all()
    adopted_pets = Pet.query.filter_by(available=False).all()
    return render_template("list_pets.html", adoptable_pets=adoptable_pets, adopted_pets=adopted_pets)

@app.route('/<int:pet_id>')
def show_pet_details(pet_id):
    """Show a detailed page of a pet."""
    pet = Pet.query.get_or_404(pet_id)
    return render_template("pet_details.html", pet=pet)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Add a new pet."""
    form = AddPetForm()
    if form.validate_on_submit():       
        data = form.data
        del data['csrf_token']
        pet = Pet(**data)
        db.session.add(pet)
        db.session.commit()

        flash(f'{pet.name} has been added!')
        return redirect('/')
    else:
        return render_template("add_pet_form.html", form=form)

@app.route('/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Edit info for a specific pet."""
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        data = form.data
        del data['csrf_token']
        for key, value in data.items():
            setattr(pet, key, value)

        db.session.commit()
        flash(f'{pet.name} has been updated!')
        return redirect(f'/{pet.id}')
    else:
        return render_template("edit_pet_form.html", form=form)
