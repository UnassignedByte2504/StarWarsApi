"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import json
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, Species, Vehicle, Starship, Films, Character
#from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code





# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


# get planets from db and convert to json for response



@app.route('/planets', methods=['GET'])

def handle_planet():
   
    
    response_body = {
        "msg": "Hello, this is your GET /planet response ", 
    }

    return jsonify(response_body), 200


@app.route('/planets/<int:planet_id>', methods=['GET'])
def handle_planet_id(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        raise APIException('No planet found', status_code=404)
    response_body = {
        "msg": "Hello, this is your GET /planet/<planet_id> response ",
        "planet": planet
    }

    return json.dumps(response_body), 200


@app.route('/species', methods=['GET'])
def handle_species():
    Species = Species.query.all()
    response_body = {
        "msg": "Hello, this is your GET /species response ",
        "species": Species 
    }

    return jsonify(response_body), 200


@app.route('/species/<int:species_id>', methods=['GET'])
def handle_species_id (species_id):
    species = Species.query.get(species_id)
    if species is None:
        raise APIException('No species found', status_code=404)
    response_body = {
        "msg": "Hello, this is your GET /species/<species_id> response ",
        "species": species
    }

    return jsonify(response_body), 200



@app.route('/vehicles', methods=['GET'])
def handle_vehicle():
    Vehicles = Vehicle.query.all()
    response_body = {
        "msg": "Hello, this is your GET /vehicle response ",
        "vehicle ": Vehicles
    }

    return jsonify(response_body), 200


@app.route('/vehicle/<int:vehicle_id>', methods=['GET'])
def handle_vehicle_id(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    if vehicle is None:
        raise APIException('No vehicle found', status_code=404)
    response_body = {
        "msg": "Hello, this is your GET /vehicle/<vehicle_id> response ",
        "vehicle": vehicle 
    }

    return jsonify(response_body), 200


@app.route('/starships', methods=['GET'])
def handle_starship():
    Starship = Starship.query.all()
    response_body = {
        "msg": "Hello, this is your GET /starship response ",
        "starship ": Starship
    }

    return jsonify(response_body), 200


@app.route('/starships/<int:starship_id>', methods=['GET'])
def handle_starship_id(starship_id):
    starship = Starship.query.get(starship_id)
    if starship is None:
        raise APIException('No starship found', status_code=404)
    response_body = {
        "msg": "Hello, this is your GET / starships/<starship_id> response ",
        "starship": starship 
    }

    return jsonify(response_body), 200



@app.route('/films', methods=['GET'])
def handle_film():
    Films = Films.query.all()
    response_body = {
        "msg": "Hello, this is your GET /films response ",
        "film ": Films
    }

    return jsonify(response_body), 200


@app.route('/films/<int:film_id>', methods=['GET'])
def handle_film_id(film_id):
    Film = Films.query.get(film_id)
    if Film is None:
        raise APIException('No film found', status_code=404)
    response_body = {
        "msg": "Hello, this is your GET /film/<film_id> response ",
        "film": Film
    }

    return jsonify(response_body), 200


@app.route('/character', methods=['GET'])
def handle_character():
    Character = Character.query.all()
    response_body = {
        "msg": "Hello, this is your GET /character response ",
        "character ": Character
    }

    return jsonify(response_body), 200


@app.route('/character/<int:character_id>', methods=['GET'])
def handle_character_id(character_id):
    character = Character.query.get(character_id)
    if character is None:
        raise APIException('No character found', status_code=404)
    response_body = {
        "msg": "Hello, this is your GET /character/<character_id> response ",
        "character": character 
    }

    return jsonify(response_body), 200




# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
