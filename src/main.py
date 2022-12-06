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
from models import db, User, Planet, Species, Vehicle, Starship, Films, Character, Favourites

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

@app.route('/planets', methods=['GET', 'POST'])
def handle_planet():
    if request.method == 'GET':
        # GET requests
        planet_query = Planet.query.all()
        all_planets = list(map(lambda x: x.serialize(), planet_query))
        return jsonify(all_planets), 200

    elif request.method == 'POST':
        # POST requests
        data = request.get_json(force=True) 
        new_planet = Planet(
            name=data['name'],
            rotation_period=data['rotation_period'],
            orbital_period=data['orbital_period'],
            diameter=data['diameter'],
            climate=data['climate'],
            gravity=data['gravity'],
            terrain=data['terrain'],
            surface_water=data['surface_water'],
            population=data['population'],
            residents=data['residents'],
            films=data['films'],
            created=data['created'],
            edited=data['edited'],
            url=data['url']
        )
        db.session.add(new_planet)
        db.session.commit()
        return jsonify(new_planet.serialize()), 201

@app.route('/planets/<int:planet_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_planet_id(planet_id):

    planet_query = Planet.query.get(planet_id)
    if planet_query is None:
        return jsonify({'msg': 'Planet not found'}), 404
    if request.method == 'GET':
        # GET requests
        return jsonify(planet_query.serialize()), 200
    elif request.method == 'PUT':
        # UPDATE requests
        data = request.get_json(force=True)  
        planet = Planet.query.get(planet_id)
        planet.name = data['name']
        planet.rotation_period = data['rotation_period']
        planet.orbital_period = data['orbital_period']
        planet.diameter = data['diameter']
        planet.climate = data['climate']
        planet.gravity = data['gravity']
        planet.terrain = data['terrain']
        planet.surface_water = data['surface_water']
        planet.population = data['population']
        planet.residents = data['residents']
        planet.films = data['films']
        planet.created = data['created']
        planet.edited = data['edited']
        planet.url = data['url']
        db.session.commit()
        return jsonify(planet.serialize()), 200
    elif request.method == 'DELETE':
        # DELETE requests
        db.session.delete(planet_query)
        db.session.commit()
        return jsonify({'msg': 'Planet deleted'}), 200


@app.route('/species', methods=['GET', 'POST'])
def handle_species():
    if request.method == 'GET':
        # GET requests
        species_query = Species.query.all()
        all_species = list(map(lambda x: x.serialize(), species_query))
        return jsonify(all_species), 200
    elif request.method == 'POST':
        # POST requests
        data = request.get_json(force=True)
        new_species = Species(
            name=data['name'],
            classification = data['classification'],
            designation = data['designation'],
            average_height = data['average_height'],
            skin_colors = data['skin_colors'],
            hair_colors = data['hair_colors'],
            eye_colors = data['eye_colors'],
            average_lifespan = data['average_lifespan'],
            homeworld = data['homeworld'],
            language = data['language'],
            people = data['people'],
            films = data['films'],
            created = data['created'],
            edited = data['edited'],
            url = data['url']
            )
        db.session.add(new_species)
        db.session.commit()
        return jsonify(new_species.serialize()), 201
            

@app.route('/species/<int:species_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_species_id (species_id):
    species_query = Species.query.get(species_id)
    if request.method == 'GET':
        # GET requests
        if species_query:
            return jsonify(species_query.serialize()), 200
        else:
            return jsonify({'msg': 'Species not found'}), 404
        #UPDATE request
    elif request.method == 'PUT':
            data = request.get_json(force=True)
            specie = Species.query.get(species_id)
            specie.name = data['name']
            specie.classification = data['classification']
            specie.designation = data['designation']
            specie.average_height = data['average_height']
            specie.skin_colors = data['skin_colors']
            specie.hair_colors = data['hair_colors']
            specie.eye_colors = data['eye_colors']
            specie.average_lifespan = data['average_lifespan']
            specie.homeworld = data['homeworld']
            specie.language = data['language']
            specie.people = data['people']
            specie.films = data['films']
            specie.created = data['created']
            specie.edited = data['edited']
            specie.url = data['url']
            db.session.commit()
            return jsonify(specie.serialize()), 200
        #DELELETE request
    elif request.method == 'DELETE':
            specie = Species.query.get(species_id)
            if specie: 
                db.session.delete(specie)
                db.session.commit()
                return jsonify({'msg': 'Species deleted'}), 200
            else:
                return jsonify({'msg': 'Species not found'}), 404



@app.route('/vehicles', methods=['GET', 'POST'])
def handle_vehicle():
    #GET request
    if request.method == 'GET':
        vehicle_query = Vehicle.query.all()
        all_vehicles = list(map(lambda x: x.serialize(), vehicle_query))
        return jsonify(all_vehicles), 200
    #POST request
    elif request.method == 'POST':
        data = request.get_json(force=True)
        vehicle = Vehicle(
            name = data['name'],
            model = data['model'],
            vehicle_class = data['vehicle_class'],
            manufacturer = data['manufacturer'],
            cost_in_credits = data['cost_in_credits'],
            length = data['length'],
            crew= data['crew'],
            passengers = data['passengers'],
            max_atmosphering_speed = data['max_atmosphering_speed'],
            cargo_capacity = data['cargo_capacity'],
            consumables = data['consumables'],
            films= data['films'],
            pilots = data['pilots'],
            created= data['created'],
            edited= data['edited'],
            url= data['url']
        )
        db.session.add(vehicle)
        db.session.commit()
        return jsonify(vehicle.serialize()), 201
         
@app.route('/vehicles/<int:vehicle_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_vehicle_id(vehicle_id):
    vehicle_query = Vehicle.query.get(vehicle_id)
    #GET request
    if request.method == 'GET':
        if vehicle_query:
            return jsonify(vehicle_query.serialize()), 200
        else:
            return jsonify({'msg': 'Vehicle not found'}), 404
    #PUT request
    elif request.method == 'PUT':
        data = request.get_json(force=True)
        if vehicle_query:
            vehicle_query.name = data['name']
            vehicle_query.model = data['model']
            vehicle_query.manufacturer = data['manufacturer']
            vehicle_query.cost_in_credits = data['cost_in_credits']
            vehicle_query.length = data['length']
            vehicle_query.crew= data['crew']
            vehicle_query.passengers = data['passengers']
            vehicle_query.max_atmosphering_speed = data['max_atmosphering_speed']
            vehicle_query.cargo_capacity = data['cargo_capacity']
            vehicle_query.consumables = data['consumables']
            vehicle_query.films = data['films']
            vehicle_query.pilots = data['pilots']
            vehicle_query.created = data['created']
            vehicle_query.edited = data['edited']
            vehicle_query.url = data['url']
            db.session.commit()
            return jsonify(vehicle_query.serialize()), 200

        else:
            return jsonify({'msg': 'Vehicle not found'}), 404
    #DELETE request
    elif request.method == 'DELETE':
        if vehicle_query:
            db.session.delete(vehicle_query)
            db.session.commit()
            return jsonify({'msg': 'Vehicle deleted'}), 200

        else:
            return jsonify({'msg': 'Vehicle not found'}), 404


@app.route('/starships', methods=['GET', 'POST'])
def handle_starship():
    starship_query = Starship.query.all()
    #GET request
    if request.method == 'GET':
        all_starships = list(map(lambda x: x.serialize(), starship_query))
        return jsonify(all_starships), 200
    #POST request
    elif request.method == 'POST':
        data = request.get_json(force=True)
        new_starship = Starship(
            name = data['name'],
            model = data['model'],
            starship_class = data['starship_class'],
            manufacturer = data['manufacturer'],
            cost_in_credits = data['cost_in_credits'],
            length = data['length'],
            crew = data['crew'],
            passengers = data['passengers'],
            max_atmosphering_speed = data['max_atmosphering_speed'],
            hyperdrive_rating = data['hyperdrive_rating'],
            MGLT = data['MGLT'],
            cargo_capacity = data['cargo_capacity'],
            consumables = data['consumables'],
            films = data['films'],
            pilots = data['pilots'],
            created = data['created'],
            edited = data['edited'],
            url = data['url']
            )
        db.session.add(new_starship)
        db.session.commit()
        return jsonify(new_starship.serialize()), 201


@app.route('/starships/<int:starship_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_starship_id(starship_id):
    starship_query = Starship.query.get(starship_id)
    if request.method == 'GET':
        if starship_query:
            return jsonify(starship_query.serialize()), 200

        else:
            return jsonify({'msg': 'Starship not found'}), 404
    elif request.method == 'PUT':
        if starship_query:
            data = request.get_json(force=True)
            starship_query.name = data['name']
            starship_query.model = data['model']
            starship_query.starship_class = data['starship_class']
            starship_query.manufacturer = data['manufacturer']
            starship_query.cost_in_credits = data['cost_in_credits']
            starship_query.length = data['length']
            starship_query.crew = data['crew']
            starship_query.passengers = data['passengers']
            starship_query.max_atmosphering_speed = data['max_atmosphering_speed']
            starship_query.hyperdrive_rating = data['hyperdrive_rating']
            starship_query.mglt = data['mglt']
            starship_query.cargo_capacity = data['cargo_capacity']
            starship_query.consumables = data['consumables']
            starship_query.films = data['films']
            starship_query.pilots = data['pilots']
            starship_query.created = data['created']
            starship_query.edited = data['edited']
            starship_query.url = data['url']
            db.session.commit()
            return jsonify(starship_query.serialize()), 200

    elif request.method == 'DELETE':
        if starship_query:
            db.session.delete(starship_query)
            db.session.commit()
            return jsonify({'msg': 'Starship deleted'}), 200

@app.route('/films', methods=['GET', 'POST'])
def handle_film():
    film_query = Films.query.all()

    if request.method == 'GET':
        all_films= list(map(lambda x: x.serialize(), film_query))
        return jsonify(all_films), 200

    elif request.method == 'POST':
        data = request.get_json(force=True)
        new_film = Film(
            title = data['title'],
            episode_id = data['episode_id'],
            opening_crawl = data['opening_crawl'],
            director = data['director'],
            producer = data['producer'],
            release_date = data['release_date'],
            characters = data['characters'],
            planets = data['planets'],
            starships = data['starships'],
            vehicles = data['vehicles'],
            species = data['species'],
            created = data['created'],
            edited = data['edited'],
            url = data['url']
        )
        db.session.add(new_film)
        db.session.commit()
        return jsonify(new_film.serialize()), 200

@app.route('/films/<int:film_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_film_id(film_id):
    film_query = Films.query.get(film_id)

    if request.method == 'GET':
        if film_query:
            return jsonify(film_query.serialize()), 200
        else:
            return jsonify({'msg': 'Film not found'}), 404

    elif request.method == 'PUT':
        data = request.get_json(force=True)
        if film_query:
            film_query.title = data['title']
            film_query.episode_id = data['episode_id']
            film_query.opening_crawl = data['opening_crawl']
            film_query.director = data['director']
            film_query.producer = data['producer']
            film_query.release_date = data['release_date']
            film_query.characters = data['characters']
            film_query.planets = data['planets']
            film_query.starships = data['starships']
            film_query.vehicles = data['vehicles']
            film_query.species = data['species']
            film_query.created = data['created']
            film_query.edited = data['edited']
            film_query.url = data['url']
            db.session.commit()
            return jsonify({'msg': 'Film updated'}, film_query.serialize()), 200  
        else:
            return jsonify({'msg': 'Film not found'}), 404
    #DELETE request
    elif request.method == 'DELETE':
        if film_query:
            db.session.delete(film_query)
            db.session.commit()
            return jsonify({'msg': 'Film deleted'}), 200
        else:
            return jsonify({'msg': 'Film not found'}), 404

@app.route('/characters', methods=['GET', 'POST'])
def handle_character():
    #GET request
    if request.method == 'GET':
        character_query = Character.query.all()
        all_characters = list(map(lambda x: x.serialize(), character_query))
        return jsonify(all_characters), 200
    #POST request
    elif request.method == 'POST':
        data = request.get_json(force=True)
        new_character = Character(
            name = data['name'],
            height = data['height'],
            mass = data['mass'],
            hair_color = data['hair_color'],
            skin_color = data['skin_color'],
            eye_color = data['eye_color'],
            birth_year = data['birth_year'],
            gender = data['gender'],
            homeworld = data['homeworld'],
            films = data['films'],
            species = data['species'],
            vehicles = data['vehicles'],
            starships = data['starships'],
            created = data['created'],
            edited = data['edited'],
            url = data['url']
        )
        db.session.add(new_character)
        db.session.commit()
        return jsonify({'msg': 'Character added'}, new_character.serialize()), 201


@app.route('/characters/<int:character_id>', methods=['GET','PUT','DELETE'])
def handle_character_id(character_id):
    character_query = Character.query.get(character_id)
    #GET request
    if request.method == 'GET':
        if character_query:
            return jsonify(character_query.serialize()), 200
        else:
            return jsonify({'msg': 'Character not found'}), 404
    #PUT request
    elif request.method == 'PUT':
        data = request.get_json(force=True)
        if character_query:
            character_query.name = data['name']
            character_query.height = data['height']
            character_query.mass = data['mass']
            character_query.hair_color = data['hair_color']
            character_query.skin_color = data['skin_color']
            character_query.eye_color = data['eye_color']
            character_query.birth_year = data['birth_year']
            character_query.gender = data['gender']
            character_query.homeworld = data['homeworld']
            character_query.films = data['films']
            character_query.species = data['species']
            character_query.vehicles = data['vehicles']
            character_query.starships = data['starships']
            character_query.created = data['created']
            character_query.edited = data['edited']
            character_query.url = data['url']
            db.session.commit()
            return jsonify({'msg': 'Character updated'}, character_query.serialize())
        else:
            return jsonify({'msg': 'Character not found'}), 404
    #DELETE request
    elif request.method == 'DELETE':
        if character_query:
            db.session.delete(character_query)
            db.session.commit()
            return jsonify({'msg': 'Character deleted'}), 200
        else:
            return jsonify({'msg': 'Character not found'}), 404


@app.route('/favs', methods=['GET','POST'])
def handle_favs():
    #GET request
    if request.method == 'GET':
        favs = Favourites.query.all()
        favs_list = []
        for fav in favs:
            favs_list.append(fav.serialize())
        return jsonify(favs_list), 200
    #POST request
    if request.method == 'POST':
        data = request.get_json(force=True)
        fav = Favourites( user_id = data['user_id'], character_id = data['character_id'])
        db.session.add(fav)
        db.session.commit()
        return jsonify({'msg': 'Character added to favourites'}), 200
@app.route('/favs/<int:fav_id>', methods=['GET','DELETE'])
def handle_favs_id(fav_id):
    if request.method == 'GET':
        fav = Favourites.query.get(fav_id)
        if fav:
            return jsonify(fav.serialize()), 200
    if request.method == 'DELETE':
        fav = Favourites.query.get(fav_id)
        if fav:
            db.session.delete(fav)
            db.session.commit()
            return jsonify({'msg': 'Character removed from favourites'}), 200




# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
