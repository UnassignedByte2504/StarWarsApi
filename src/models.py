from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Date, create_engine, MetaData, Table
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    birth_date = db.Column(db.Date(), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Friendship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    friend_id = db.Column(db.Integer, ForeignKey('user.id'))


class Thread(db.Model):
    __tablename__ = 'thread'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    message = db.Column(db.String(250), nullable=True)
    user = relationship(User)


class Forum (db.Model):
    __tablename__ = 'forum'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    thread_id = db.Column(db.Integer, ForeignKey('thread.id'))
    user = relationship(User)
    thread = relationship(Thread)


class Private_message(db.Model):
    __tablename__ = 'private_message'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    message = db.Column(db.String(250), nullable=False)
    user = relationship(User)


class User_session(db.Model):
    __tablename__ = 'user_session'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    token = db.Column(db.String(250), nullable=False)
    user = relationship(User)


class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    rotation_period = db.Column(db.Integer, nullable=True)
    orbital_period = db.Column(db.Integer, nullable=True)
    diameter = db.Column(db.Integer, nullable=True)
    climate = db.Column(db.String(250), nullable=True)
    gravity = db.Column(db.String(250), nullable=True)
    terrain = db.Column(db.String(250), nullable=True)
    surface_water = db.Column(db.Integer, nullable=True)
    population = db.Column(db.Integer, nullable=True)
    residents = db.Column(db.String(250), nullable=True)
    films = db.Column(db.String(250), nullable=True)
    created = db.Column(db.String(250), nullable=True)
    edited = db.Column(db.String(250), nullable=True)
    url = db.Column(db.String(250), nullable=True)

    def __repr__ (self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'rotation_period': self.rotation_period,
            'orbital_period': self.orbital_period,
            'diameter': self.diameter,
            'climate': self.climate,
            'gravity': self.gravity,
            'terrain': self.terrain,
            'surface_water': self.surface_water,
            'population': self.population,
            'residents': self.residents,
            'films': self.films,
            'created': self.created,
            'edited': self.edited,
            'url': self.url
            }


class Films(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    episode_id = db.Column(db.Integer, nullable=True)
    opening_crawl = db.Column(db.String(250), nullable=True)
    director = db.Column(db.String(250), nullable=True)
    producer = db.Column(db.String(250), nullable=True)
    release_date = db.Column(db.String(250), nullable=True)
    characters = db.Column(db.String(250), nullable=True)
    planets = db.Column(db.String(250), nullable=True)
    starships = db.Column(db.String(250), nullable=True)
    vehicles = db.Column(db.String(250), nullable=True)
    species = db.Column(db.String(250), nullable=True)
    created = db.Column(db.String(250), nullable=True)
    edited = db.Column(db.String(250), nullable=True)
    url = db.Column(db.String(250), nullable=True)

    def __repr__ (self):
        return '<Films %r>' % self.title 

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'episode_id': self.episode_id,
            'opening_crawl': self.opening_crawl,
            'director': self.director,
            'producer': self.producer,
            'release_date': self.release_date,
            'characters': self.characters,
            'planets': self.planets,
            'starships': self.starships,
            'vehicles': self.vehicles,
            'species': self.species,
            'created': self.created,
            'edited': self.edited,
            'url': self.url
            }


class Starship(db.Model):
    __tablename__ = 'starship'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=True)
    starship_class = db.Column(db.String(250), nullable=True)
    manufacturer = db.Column(db.String(250), nullable=True)
    cost_in_credits = db.Column(db.Integer, nullable=True)
    length = db.Column(db.Integer, nullable=True)
    crew = db.Column(db.Integer, nullable=True)
    passengers = db.Column(db.Integer, nullable=True)
    max_atmosphering_speed = db.Column(db.Integer, nullable=True)
    hyperdrive_rating = db.Column(db.Integer, nullable=True)
    mglt = db.Column(db.Integer, nullable=True)
    cargo_capacity = db.Column(db.Integer, nullable=True)
    consumables = db.Column(db.String(250), nullable=True)
    films = db.Column(db.String(250), nullable=True)
    pilots = db.Column(db.String(250), nullable=True)
    created = db.Column(db.String(250), nullable=True)
    edited = db.Column(db.String(250), nullable=True)
    url = db.Column(db.String(250), nullable=True)

    def __repr__ (self):
        return '<Starship %r>' % self.name 

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'starship_class': self.starship_class,
            'manufacturer': self.manufacturer,
            'cost_in_credits': self.cost_in_credits,
            'length': self.length,
            'crew': self.crew,
            'passengers': self.passengers,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'hyperdrive_rating': self.hyperdrive_rating,
            'mglt': self.mglt,
            'cargo_capacity': self.cargo_capacity,
            'consumables': self.consumables,
            'films': self.films,
            'pilots': self.pilots,
            'created': self.created,
            'edited': self.edited,
            'url': self.url
            }

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=True)
    vehicle_class = db.Column(db.String(250), nullable=True)
    manufacturer = db.Column(db.String(250), nullable=True)
    cost_in_credits = db.Column(db.Integer, nullable=True)
    length = db.Column(db.Integer, nullable=True)
    crew = db.Column(db.Integer, nullable=True)
    passengers = db.Column(db.Integer, nullable=True)
    max_atmosphering_speed = db.Column(db.Integer, nullable=True)
    cargo_capacity = db.Column(db.Integer, nullable=True)
    consumables = db.Column(db.String(250), nullable=True)
    films = db.Column(db.String(250), nullable=True)
    pilots = db.Column(db.String(250), nullable=True)
    created = db.Column(db.String(250), nullable=True)
    edited = db.Column(db.String(250), nullable=True)
    url = db.Column(db.String(250), nullable=True)

    def __repr__ (self):
        return '<Vehicle %r>' % self.name 

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'vehicle_class': self.vehicle_class,
            'manufacturer': self.manufacturer,
            'cost_in_credits': self.cost_in_credits,
            'length': self.length,
            'crew': self.crew,
            'passengers': self.passengers,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'cargo_capacity': self.cargo_capacity,
            'consumables': self.consumables,
            'films': self.films,
            'pilots': self.pilots,
            'created': self.created,
            'edited': self.edited,
            'url': self.url
            }

class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    classification = db.Column(db.String(250), nullable=True)
    designation = db.Column(db.String(250), nullable=True)
    average_height = db.Column(db.Integer, nullable=True)
    skin_colors = db.Column(db.String(250), nullable=True)
    hair_colors = db.Column(db.String(250), nullable=True)
    eye_colors = db.Column(db.String(250), nullable=True)
    average_lifespan = db.Column(db.Integer, nullable=True)
    homeworld = db.Column(db.String(250), nullable=True)
    language = db.Column(db.String(250), nullable=True)
    people = db.Column(db.String(250), nullable=True)
    films = db.Column(db.String(250), nullable=True)
    created = db.Column(db.String(250), nullable=True)
    edited = db.Column(db.String(250), nullable=True)
    url = db.Column(db.String(250), nullable=True)

    def __repr__ (self):
        return '<Species %r>' % self.name 

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'classification': self.classification,
            'designation': self.designation,
            'average_height': self.average_height,
            'skin_colors': self.skin_colors,
            'hair_colors': self.hair_colors,
            'eye_colors': self.eye_colors,
            'average_lifespan': self.average_lifespan,
            'homeworld': self.homeworld,
            'language': self.language,
            'people': self.people,
            'films': self.films,
            'created': self.created,
            'edited': self.edited,
            'url': self.url
            }

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer, nullable=True)
    mass = db.Column(db.Integer, nullable=True)
    hair_color = db.Column(db.String(250), nullable=True)
    skin_color = db.Column(db.String(250), nullable=True)
    eye_color = db.Column(db.String(250), nullable=True)
    birth_year = db.Column(db.String(250), nullable=True)
    gender = db.Column(db.String(250), nullable=True)
    homeworld = db.Column(db.String(250),  nullable=True)
    films = db.Column(db.String(250), nullable=True)
    species = db.Column(db.String(250),  nullable=True)
    vehicles = db.Column(db.String(250),  nullable=True)
    starships = db.Column(db.String(250),  nullable=True)
    created = db.Column(db.String(250), nullable=True)
    edited = db.Column(db.String(250), nullable=True)
    url = db.Column(db.String(250), nullable=True)

    def __repr__ (self):
        return '<Character %r>' % self.name 

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'mass': self.mass,
            'hair_color': self.hair_color,
            'skin_color': self.skin_color,
            'eye_color': self.eye_color,
            'birth_year': self.birth_year,
            'gender': self.gender,
            'homeworld': self.homeworld,
            'films': self.films,
            'species': self.species,
            'vehicles': self.vehicles,
            'starships': self.starships,
            'created': self.created,
            'edited': self.edited,
            'url': self.url
            }


class Favourites(db.Model):
    __tablename__ = 'favourites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = db.Column(db.Integer, ForeignKey('character.id'))
    character = relationship(Character)
    planet_id = db.Column(db.Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    vehicle_id = db.Column(db.Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(Vehicle)
    species_id = db.Column(db.Integer, ForeignKey('species.id'))
    species = relationship(Species)
    starship_id = db.Column(db.Integer, ForeignKey('starship.id'))
    starship = relationship(Starship)
    films_id = db.Column(db.Integer, ForeignKey('films.id'))
    films = relationship(Films)

    def __repr__ (self):
        return '<Favourites %r>' % self.id 

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'character_id': self.character_id,
            'planet_id': self.planet_id,
            'vehicle_id': self.vehicle_id,
            'species_id': self.species,
            'starship_id': self.starship_id,
            'films_id': self.films_id
            }

class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)

