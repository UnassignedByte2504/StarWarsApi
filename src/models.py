from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Date
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    birth_date = db.Column(db.Date(), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

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
    message = db.Column(db.String(250), nullable=False)
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
    rotation_period = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    surface_water = db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    residents = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)


class Films(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    episode_id = db.Column(db.Integer, nullable=False)
    opening_crawl = db.Column(db.String(250), nullable=False)
    director = db.Column(db.String(250), nullable=False)
    producer = db.Column(db.String(250), nullable=False)
    release_date = db.Column(db.String(250), nullable=False)
    characters = db.Column(db.String(250), nullable=False)
    planets = db.Column(db.String(250), nullable=False)
    starships = db.Column(db.String(250), nullable=False)
    vehicles = db.Column(db.String(250), nullable=False)
    species = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)


class Starship(db.Model):
    __tablename__ = 'starship'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    starship_class = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    cost_in_credits = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    crew = db.Column(db.Integer, nullable=False)
    passengers = db.Column(db.Integer, nullable=False)
    max_atmosphering_speed = db.Column(db.Integer, nullable=False)
    hyperdrive_rating = db.Column(db.Integer, nullable=False)
    mglt = db.Column(db.Integer, nullable=False)
    cargo_capacity = db.Column(db.Integer, nullable=False)
    consumables = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)
    pilots = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)


class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    vehicle_class = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    cost_in_credits = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    crew = db.Column(db.Integer, nullable=False)
    passengers = db.Column(db.Integer, nullable=False)
    max_atmosphering_speed = db.Column(db.Integer, nullable=False)
    cargo_capacity = db.Column(db.Integer, nullable=False)
    consumables = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)
    pilots = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)


class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    classification = db.Column(db.String(250), nullable=False)
    designation = db.Column(db.String(250), nullable=False)
    average_height = db.Column(db.Integer, nullable=False)
    skin_colors = db.Column(db.String(250), nullable=False)
    hair_colors = db.Column(db.String(250), nullable=False)
    eye_colors = db.Column(db.String(250), nullable=False)
    average_lifespan = db.Column(db.Integer, nullable=False)
    homeworld = db.Column(db.String(250), nullable=False)
    language = db.Column(db.String(250), nullable=False)
    people = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)


class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    homeworld = db.Column(db.String(250),  nullable=False)
    films = db.Column(db.String(250), nullable=False)
    species = db.Column(db.String(250),  nullable=False)
    vehicles = db.Column(db.String(250),  nullable=False)
    starships = db.Column(db.String(250),  nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)


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

class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)

